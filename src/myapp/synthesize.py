from django.core.files import File
from .models import Document
import os
import time

def synthesize(file_dir):
    time.sleep(5)
    with open(file_dir, 'rb') as orignal_video:
        name = os.path.basename(orignal_video.name)
        newName = name.split('.')[0]+'_synthesized.mp4'
        doc = Document()
        doc.docfile.save(newName, File(orignal_video))