from django.shortcuts import render,redirect
from .forms import FormPost
from .models import Post
from django.views.generic import ListView, View

# Create your views here.


#cria a classe novoPost para gerenciar as funções de postagem usando atributos de classe para armazenar os posts em memória
class novoPost(View):
    model = Post
    classe_form = FormPost
    nome_template = 'postar.html'

    def get(self, request):
        formulario = self.classe_form()
        return render(request, self.nome_template, {'formulario':formulario})

    def post(self, request):
        formulario = self.classe_form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
        return render(request, self.nome_template, {'formulario':formulario})

class listaPost(ListView):
    model = Post
    template_name = "inicio.html"
    context_object_name = 'posts'
    ordering = ['-id']








    #@classmethod #metodo da classe novoPost que gera formulário para nova postagem
   # def postar(cls, request):
        #methods = request.method
        #if methods == 'POST':
            #formulario = FormPost(request.POST, request.FILES)
            #if formulario.is_valid():
                #formulario.save()
               # return redirect('inicio')
       # else:
            #formulario = FormPost()
        
       # return render(request,'postar.html', { 'formulario':formulario })
            

            