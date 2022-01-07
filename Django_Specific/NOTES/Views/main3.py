# Built-in class-based generic views

# Display list and detail pages for a single object.
# views.py
from django.views.generic import ListView
from books.models import Publisher

class PublisherListView(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'

"""
Adding extra context¶
Often you need to present some extra information beyond that provided by the generic view. For example, think of showing a list of all the books on each publisher detail page. The DetailView generic view provides the publisher to the context, but how do we get additional information in that template?

The answer is to subclass DetailView and provide your own implementation of the get_context_data method. The default implementation adds the object being displayed to the template, but you can override it to send more:
"""

from django.views.generic import DetailView
from books.models import Book, Publisher

class PublisherDetailView(DetailView):

    model = Publisher

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context

"""
Generally, get_context_data will merge the context data of all parent classes with those of the current class. To preserve this behavior in your own classes where you want to alter the context, you should be sure to call get_context_data on the super class. When no two classes try to define the same key, this will give the expected results. However if any class attempts to override a key after parent classes have set it (after the call to super), any children of that class will also need to explicitly set it after super if they want to be sure to override all parents. If you’re having trouble, review the method resolution order of your view.

Another consideration is that the context data from class-based generic views will override data provided by context processors; see get_context_data() for an example.
"""
"""
Viewing subsets of objects¶
Now let’s take a closer look at the model argument we’ve been using all along. The model argument, which specifies the database model that the view will operate upon, is available on all the generic views that operate on a single object or a collection of objects. However, the model argument is not the only way to specify the objects that the view will operate upon – you can also specify the list of objects using the queryset argument:
"""
from django.views.generic import DetailView
from books.models import Publisher

class PublisherDetailView(DetailView):

    context_object_name = 'publisher'
    queryset = Publisher.objects.all()


######
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from books.models import Book, Publisher

class PublisherBookListView(ListView):

    template_name = 'books/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)

#########

class AuthorDetailView(DetailView):

    queryset = Author.objects.all()

    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()
        obj.save()
        return obj