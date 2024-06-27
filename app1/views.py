from django.shortcuts import render

# Create your views here.
def cond_st(request):
    d={'name':'teju','age':23,'gender':'female'}
    return render(request,'cond_st.html',context=d)