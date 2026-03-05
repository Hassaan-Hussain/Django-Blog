from blogs.models import Category, SocialLinks


def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def social_links(request):
    links = SocialLinks.objects.all()
    return dict(links=links)