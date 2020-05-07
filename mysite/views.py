from django.shortcuts import render
from .models import *


def index(request):
    banners_list = Banner.objects.filter(page_to_display=1)
    sponsors_list = Sponsor.objects.all()
    sig_head_list = Member.objects.filter(sig_head=True)
    image_gallery_full = Image.objects.all()
    image_gallery_short = Image.objects.filter(display_on_index=True)
    context = {'banners_list': banners_list,
               'sponsors_list': sponsors_list,
               'sig_head_list': sig_head_list,
               'image_gallery_full': image_gallery_full,
               'image_gallery_short': image_gallery_short,
               }
    return render(request, 'index.html', context=context)


def about(request):
    banners_list = Banner.objects.filter(page_to_display=2)
    blog_list = Blog.objects.all()
    sig_head_list = Member.objects.filter(sig_head=True)
    image_gallery_full = Image.objects.all()
    full_member_list = Member.objects.all()
    image_gallery_short = Image.objects.filter(display_on_index=True)
    context = {'banners_list': banners_list,
               'blog_list': blog_list,
               'sig_head_list': sig_head_list,
               'image_gallery_full': image_gallery_full,
               'image_gallery_short': image_gallery_short,
               'members_list': full_member_list,
               }
    return render(request, 'about.html', context=context)


def contact(request):
    banners_list = Banner.objects.filter(page_to_display=3)
    sig_head_list = Member.objects.filter(sig_head=True)
    full_member_list = Member.objects.all()
    image_gallery_full = Image.objects.all()
    image_gallery_short = Image.objects.filter(display_on_index=True)
    context = {'banners_list': banners_list,
               'sig_head_list': sig_head_list,
               'image_gallery_full': image_gallery_full,
               'image_gallery_short': image_gallery_short,
               'full_member_list': full_member_list,
               }
    return render(request, 'contact.html', context=context)


def team(request):
    full_member_list = Member.objects.all()

    banners_list = Banner.objects.filter(page_to_display=4)
    sig_head_list = Member.objects.filter(sig_head=True)
    image_gallery_full = Image.objects.all()
    image_gallery_short = Image.objects.filter(display_on_index=True)
    context = {
               'sig_head_list': sig_head_list,
               'banners_list': banners_list,
               'image_gallery_full': image_gallery_full,
               'image_gallery_short': image_gallery_short,
               'full_member_list': full_member_list
               }
    return render(request, 'team.html', context=context)


def aerodynamics(request):
    full_member_list = Member.objects.filter(sig=1)
    blog_list = Blog.objects.filter(blog_filter=1)
    banners_list = Banner.objects.filter(page_to_display=5)
    document_list = Document.objects.filter(subsystem_filter=1)
    context = {'full_member_list': full_member_list,
               'banners_list': banners_list,
               'blog_list': blog_list,
               'document_list': document_list
               }
    return render(request, 'aerodynamics.html', context=context)


def vehicledynamics(request):
        full_member_list = Member.objects.filter(sig=2)
        blog_list = Blog.objects.filter(blog_filter=2)
        banners_list = Banner.objects.filter(page_to_display=6)
        document_list = Document.objects.filter(subsystem_filter=2)
        context = {'full_member_list': full_member_list,
                   'banners_list': banners_list,
                   'blog_list': blog_list,
                   'document_list': document_list
                   }
        return render(request, 'vehicledynamics.html', context=context)


def powertrain(request):
    full_member_list = Member.objects.filter(sig=3)
    blog_list = Blog.objects.filter(blog_filter=3)
    banners_list = Banner.objects.filter(page_to_display=7)
    document_list = Document.objects.filter(subsystem_filter=3)
    context = {'full_member_list': full_member_list,
               'banners_list': banners_list,
               'blog_list': blog_list,
               'document_list': document_list
               }
    return render(request, 'powertrain.html', context=context)


def electronics(request):
    full_member_list = Member.objects.filter(sig=4)
    blog_list = Blog.objects.filter(blog_filter=4)
    banners_list = Banner.objects.filter(page_to_display=8)
    document_list = Document.objects.filter(subsystem_filter=4)
    context = {'full_member_list': full_member_list,
               'banners_list': banners_list,
               'blog_list': blog_list,
               'document_list': document_list
               }
    return render(request, 'electronics.html', context=context)


def gallery(request):
    image_gallery_full = Image.objects.all()
    image_gallery_short = Image.objects.filter(display_on_index=True)
    context = {'image_gallery_short': image_gallery_short,
               'image_gallery_full': image_gallery_full,

               }
    return render(request, 'electronics.html', context=context)
