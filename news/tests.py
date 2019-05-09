from django.test import TestCase
from .models import Editor,Article,Tags
import datetime as dt

# Create your tests here.
class EditorTestClass(TestCase):
    def setUp(self):
        self.antavio = Editor(first_name = 'Antavio', last_name = 'Njuguna',email = 'anthonynjuguna@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.antavio,Editor))

    def test_save_method(self):
        self.antavio.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)

    def test_delete_method(self):
        self.antavio.delete_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)==0)

class ArticleTestClass(TestCase):
    def setUp(self):
        # Create a new editor and save it
        self.antavio = Editor(first_name = 'Antavio', last_name = 'Njuguna',email = 'anthonynjuguna@gmail.com')
        self.antavio.save_editor()

        # Create a new tag and save it
        self.new_tag = Tags(name = 'testit')
        self.new_tag.save()

        self.new_article = Article(title = 'Test Article',post = 'Random test Post', editor = self.antavio)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        Tags.objects.all().delete()
        Article.objects.all()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2017-05-12'
        date = dt.datetime.strptime(test_date,'%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)


