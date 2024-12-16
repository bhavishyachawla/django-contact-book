from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F, Value, CharField, Q
from django.db.models.functions import Coalesce
from django.core.paginator import Paginator
from .models import Contact
from .forms import ContactForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Contact
from .forms import CustomUserCreationForm

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, 'contacts/register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # Redirect to home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'contacts/login.html', {'form': form})

# User Logout View
def user_logout(request):
    logout(request)
    return redirect('login')


def contact_list(request):
    # Get all contacts with full name concatenation and specify the output_field
    contacts = Contact.objects.all().annotate(
        full_name=Coalesce(F('first_name'), Value('')) + ' ' +
                  Coalesce(F('middle_name'), Value('')) + ' ' +
                  Coalesce(F('last_name'), Value(''))
    ).annotate(
        full_name=Coalesce(F('full_name'), Value(''), output_field=CharField())  # Ensure output field is CharField
    ).order_by('full_name')

    # Set up pagination
    paginator = Paginator(contacts, 10)  # 10 contacts per page
    page_number = request.GET.get('page')  # Get current page number from the request
    page_obj = paginator.get_page(page_number)  # Get the page object

    return render(request, 'contacts/contact_list.html', {'page_obj': page_obj})
    
def contact_list(request):
    search_query = request.GET.get('search', '')  # Get the search query from the request

    # Filter contacts based on search term across multiple fields
    contacts = Contact.objects.all()

    if search_query:
        # Use Q objects for filtering by multiple fields
        contacts = contacts.filter(
            Q(first_name__icontains=search_query) |
            Q(middle_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(phone1__icontains=search_query) |
            Q(phone2__icontains=search_query) |
            Q(address__icontains=search_query)
        )
    
    # Pagination
    page_number = request.GET.get('page')
    paginator = Paginator(contacts, 10)  # Show 10 contacts per page
    page_obj = paginator.get_page(page_number)

    return render(request, 'contacts/contact_list.html', {'page_obj': page_obj, 'search_query': search_query})

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_create.html', {'form': form})

def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_update.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contacts/contact_delete.html', {'contact': contact})