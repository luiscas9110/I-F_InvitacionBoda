from PIL import Image, ImageDraw
import glob, os
fs=glob.glob('tmp/ref/page-*.png')
out=Image.new('RGB',(1200,1950),'white')
d=ImageDraw.Draw(out)
for i,f in enumerate(fs):
 im=Image.open(f).convert('RGB'); im.thumbnail((390,600)); x=(i%3)*400; y=(i//3)*650; out.paste(im,(x,y)); d.text((x+5,y+605),os.path.basename(f),fill='black')
out.save('tmp/ref/contact.png')
