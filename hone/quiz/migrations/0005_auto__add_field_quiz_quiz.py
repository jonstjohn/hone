# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Quiz.quiz'
        db.add_column(u'quiz_quiz', 'quiz',
                      self.gf('django.db.models.fields.CharField')(default='PHP', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Quiz.quiz'
        db.delete_column(u'quiz_quiz', 'quiz')


    models = {
        u'quiz.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'correct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Question']"})
        },
        u'quiz.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Topic']"})
        },
        u'quiz.quiz': {
            'Meta': {'object_name': 'Quiz'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'questions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['quiz.Question']", 'symmetrical': 'False'}),
            'quiz': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'quiz.topic': {
            'Meta': {'object_name': 'Topic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['quiz']