from PIL import Image
from django.conf import settings

import os


class PageTitleMixin:
    page_title = ''

    def get_page_title(self):
        return self.page_title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.get_page_title()
        return context


class ImageOperations:
   
    def process_ratio(self, image, basewidth=None):
        basewidth=128 if basewidth is None else basewidth
        full_img_path = os.path.join(settings.MEDIA_ROOT, str(image))
        print ("Image name", image)
        
        try:
            img = Image.open(full_img_path)
        except FileNotFoundError:
            print("Image path not found: ", str(image))
            return False

        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        
        img.save('media/thumbnails/'+str(image))
        return img