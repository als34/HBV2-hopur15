# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SignUp'
        db.create_table(u'test_smartLabelS_signup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'test_smartLabelS', ['SignUp'])

        # Adding model 'Question'
        db.create_table(u'test_smartLabelS_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'test_smartLabelS', ['Question'])

        # Adding model 'Choice'
        db.create_table(u'test_smartLabelS_choice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['test_smartLabelS.Question'])),
            ('choice_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'test_smartLabelS', ['Choice'])


    def backwards(self, orm):
        # Deleting model 'SignUp'
        db.delete_table(u'test_smartLabelS_signup')

        # Deleting model 'Question'
        db.delete_table(u'test_smartLabelS_question')

        # Deleting model 'Choice'
        db.delete_table(u'test_smartLabelS_choice')


    models = {
        u'test_smartLabelS.choice': {
            'Meta': {'object_name': 'Choice'},
            'choice_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['test_smartLabelS.Question']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'test_smartLabelS.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'test_smartLabelS.signup': {
            'Meta': {'object_name': 'SignUp'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['test_smartLabelS']