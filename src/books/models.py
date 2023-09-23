from django.db import models
from publishers.models import Publisher
from authors.models import Author
from django.utils.text import slugify
import uuid
from django.urls import reverse


# imports for qrcode generation
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image


class BookTitle(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def books(self):
        return self.book_set.all()

    def get_absolute_url(self):
        return reverse("books:detail-book", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Book position: {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Book(models.Model):
    title = models.ForeignKey(BookTitle, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=24, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if not self.isbn:
            self.isbn = str(uuid.uuid4()).replace('-', '')[:24].lower()

            # generate qr_code
            qrcode_img = qrcode.make(self.isbn)
            canvas = Image.new('RGB', (qrcode_img.pixel_size,
                               qrcode_img.pixel_size), 'white')
            canvas.paste(qrcode_img)
            fname = f'qr_code-{self.isbn}.png'
            buffer = BytesIO()
            canvas.save(buffer, 'PNG')
            self.qr_code.save(fname, File(buffer), save=False)
            canvas.close()

        super().save(*args, **kwargs)
