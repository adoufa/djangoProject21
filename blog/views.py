from django.shortcuts import render


posts = [
    {
        'author': 'Администратор',
        'title': 'Это мой первый пост',
        'content': 'Содержимое первого поста',
        'date_posted':'12 января 2023 года'
    },
    {
        'author': 'Пользователь №1',
        'title': 'Это мой второй пост',
        'content': 'Подробное содержание второго поста',
        'date_posted':'12 января 2023 года'
    }
]
def home(request):
    context ={
        'posts': posts
              }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'О клубе Python Bytes'})


