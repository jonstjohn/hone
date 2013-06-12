# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quiz'
        db.create_table(u'quiz_quiz', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'quiz', ['Quiz'])

        # Adding M2M table for field questions on 'Quiz'
        m2m_table_name = db.shorten_name(u'quiz_quiz_questions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('quiz', models.ForeignKey(orm[u'quiz.quiz'], null=False)),
            ('question', models.ForeignKey(orm[u'quiz.question'], null=False))
        ))
        db.create_unique(m2m_table_name, ['quiz_id', 'question_id'])


    def backwards(self, orm):
        # Deleting model 'Quiz'
        db.delete_table(u'quiz_quiz')

        # Removing M2M table for field questions on 'Quiz'
        db.delete_table(db.shorten_name(u'quiz_quiz_questions'))


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
            'questions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['quiz.Question']", 'symmetrical': 'False'})
        },
        u'quiz.topic': {
            'Meta': {'object_name': 'Topic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['quiz']