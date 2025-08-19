from django.shortcuts import render

# Create your views here.
def about_view(request):
    return render (request , 'about.html') 

def home(request):
    return HttpResponse("""
     <html>
     <head>
     <title> Homepage </title>
     </head>
     <body style = "font-family: Arial , sans-serif ; background-color : #f9f9f9 ; text-align : center ; padding : 50px; " >
     <h1 style="color: #4CAF50 ; font-size : 48 px ; margin-bottom: 20px; ">
     Welcome to My Homepage 
     <h1>
     <p style+"font-size : 20px; color:#555; ">
     This is the sample homepage style in inline css.
     </p>
     <a href="/about" style="display :inline-block ; margin-top : 20px ; padding 10px 20px ; background-color : #4CAF50 ; color:white ; 
     tect-decoration: none ; border-radius: 5px " >
     Learn More
     </a>
     </body>
     </html>


    """)