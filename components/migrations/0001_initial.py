# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Package'
        db.create_table(u'components_package', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lead_count', self.gf('django.db.models.fields.IntegerField')()),
            ('lead_finish', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('lead_style', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('lead_pattern', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('package_style', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('package_material', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('footprint', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
            ('alt_footprint', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
            ('surface_mount', self.gf('django.db.models.fields.BooleanField')()),
            ('body_width', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('body_length', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('body_height', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('mass', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('pitch', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'components', ['Package'])

        # Adding model 'Family'
        db.create_table(u'components_family', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
        ))
        db.send_create_signal(u'components', ['Family'])

        # Adding model 'Group'
        db.create_table(u'components_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('family', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['components.Family'])),
        ))
        db.send_create_signal(u'components', ['Group'])

        # Adding model 'Manufacturer'
        db.create_table(u'components_manufacturer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('country', self.gf('django_countries.fields.CountryField')(max_length=2)),
            ('dscc_qml', self.gf('django.db.models.fields.BooleanField')()),
            ('escc_qml', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'components', ['Manufacturer'])

        # Adding model 'Component'
        db.create_table(u'components_component', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('standard_pn', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('manufacturer_pn', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('local_ref', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
            ('manufacturer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['components.Manufacturer'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('package', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['components.Package'])),
            ('symbol_ref', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('family', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['components.Family'])),
            ('group', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['components.Group'])),
            ('in_bom', self.gf('django.db.models.fields.BooleanField')()),
            ('radiation_tid', self.gf('django.db.models.fields.FloatField')()),
            ('radiation_see', self.gf('django.db.models.fields.FloatField')()),
            ('rha', self.gf('django.db.models.fields.BooleanField')()),
            ('spec_type', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('spec_level', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('general_spec', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('detailed_spec', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('datasheet', self.gf('filebrowser.fields.FileBrowseField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'components', ['Component'])

        # Adding model 'Project'
        db.create_table(u'components_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'components', ['Project'])

        # Adding model 'Board'
        db.create_table(u'components_board', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['components.Project'])),
        ))
        db.send_create_signal(u'components', ['Board'])

        # Adding model 'Crossreference'
        db.create_table(u'components_crossreference', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('component_1', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'xref1_components_crossreference', to=orm['components.Component'])),
            ('component_2', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'xref2_components_crossreference', to=orm['components.Component'])),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('same_pinout', self.gf('django.db.models.fields.BooleanField')()),
            ('same_package', self.gf('django.db.models.fields.BooleanField')()),
            ('same_function', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'components', ['Crossreference'])


    def backwards(self, orm):
        # Deleting model 'Package'
        db.delete_table(u'components_package')

        # Deleting model 'Family'
        db.delete_table(u'components_family')

        # Deleting model 'Group'
        db.delete_table(u'components_group')

        # Deleting model 'Manufacturer'
        db.delete_table(u'components_manufacturer')

        # Deleting model 'Component'
        db.delete_table(u'components_component')

        # Deleting model 'Project'
        db.delete_table(u'components_project')

        # Deleting model 'Board'
        db.delete_table(u'components_board')

        # Deleting model 'Crossreference'
        db.delete_table(u'components_crossreference')


    models = {
        u'components.board': {
            'Meta': {'object_name': 'Board'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['components.Project']"})
        },
        u'components.component': {
            'Meta': {'object_name': 'Component'},
            'crossreference': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['components.Component']", 'through': u"orm['components.Crossreference']", 'symmetrical': 'False'}),
            'datasheet': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'detailed_spec': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'family': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['components.Family']"}),
            'general_spec': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'group': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['components.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_bom': ('django.db.models.fields.BooleanField', [], {}),
            'local_ref': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['components.Manufacturer']"}),
            'manufacturer_pn': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['components.Package']"}),
            'radiation_see': ('django.db.models.fields.FloatField', [], {}),
            'radiation_tid': ('django.db.models.fields.FloatField', [], {}),
            'rha': ('django.db.models.fields.BooleanField', [], {}),
            'spec_level': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'spec_type': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'standard_pn': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'symbol_ref': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'components.crossreference': {
            'Meta': {'object_name': 'Crossreference'},
            'component_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'xref1_components_crossreference'", 'to': u"orm['components.Component']"}),
            'component_2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'xref2_components_crossreference'", 'to': u"orm['components.Component']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'same_function': ('django.db.models.fields.BooleanField', [], {}),
            'same_package': ('django.db.models.fields.BooleanField', [], {}),
            'same_pinout': ('django.db.models.fields.BooleanField', [], {}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'components.family': {
            'Meta': {'object_name': 'Family'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'components.group': {
            'Meta': {'object_name': 'Group'},
            'family': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['components.Family']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'number': ('django.db.models.fields.IntegerField', [], {})
        },
        u'components.manufacturer': {
            'Meta': {'object_name': 'Manufacturer'},
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'dscc_qml': ('django.db.models.fields.BooleanField', [], {}),
            'escc_qml': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'components.package': {
            'Meta': {'object_name': 'Package'},
            'alt_footprint': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'body_height': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'body_length': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'body_width': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'footprint': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lead_count': ('django.db.models.fields.IntegerField', [], {}),
            'lead_finish': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'lead_pattern': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'lead_style': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'mass': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'package_material': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'package_style': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'pitch': ('django.db.models.fields.FloatField', [], {}),
            'surface_mount': ('django.db.models.fields.BooleanField', [], {})
        },
        u'components.project': {
            'Meta': {'object_name': 'Project'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['components']