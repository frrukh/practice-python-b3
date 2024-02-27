from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''
to render the html template first we have to create templates folder 
in our app and place the html files in it and then use render function
that is imported from django.shortcuts by default.
The render function takes at least two parameters 1.request 
2.html file name with extension.
'''
def render_html(request):
    return render(request,'render_html.html')

# getting a value from url
def get_value(request,id):
    return HttpResponse(f'<h1>the id is: "{id}"</h1>')

    
# getting a value of specific datatype.
def get_specific(request,id):
    return HttpResponse(f'<h1>the id is: "{id}"</h1>')


# sending data to html file.
def send_data(request):
    string = 'Hamid'
    integer = 23
    float = 90.5
    boolean = True
    List = [1,3,'list',False]
    tuple = (1,2,3,4,5,6)
    dictionary = {'a':1,'b':2,'c':3}
    '''
    to send data to html we have to sent all the data in last parameter 
    as a dictionary of key value pairs and in html we can get these with 
    their keys.
    '''
    return render(request,'get_data.html',{'s':string,'i':integer,'f':float,'b':boolean,'l':List,'t':tuple,'d':dictionary})


def bisects(request):
    products = [
                    {
                        'name' : 'TUC',
                        'details' : [
                                {
                                    'size' : 'half roll',
                                    'quantity' : 1000,
                                    'price' : 50
                                },
                                {
                                    'size' : 'Tiki pack',
                                    'quantity' : 1500,
                                    'price' : 20
                                }
                            ]
                    },
                    {
                        'name' : 'OREO',
                        'details' : [
                                {
                                    'size' : 'half roll',
                                    'quantity' : 2000,
                                    'price' : 80
                                },
                                {
                                    'size' : 'Tiki pack',
                                    'quantity' : 1000,
                                    'price' : 20
                                }
                            ]
                    }
                ]
    return render(request,'bisects.html',{'products':products})