# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Question.topic'
        db.add_column(u'quiz_question', 'topic',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['quiz.Topic']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Question.topic'
        db.delete_column(u'quiz_question', 'topic_id')


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
        u'quiz.topic': {
            'Meta': {'object_name': 'Topic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['quiz']