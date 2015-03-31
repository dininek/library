import pysvn, os.path, re, sys
from django.db import models
from django.forms import fields


class SVNFilePathField(models.fields.Field):
	description = "SVN File Path"
	def __init__(self, verbose_name=None, name=None, path='', match=None,
			recursive=False, allow_files=True, allow_folders=False,
			full_path=False, username='', password='', **kwargs):
		self.path, self.match, self.recursive = path, match, recursive
		self.allow_files, self.allow_folders = allow_files, allow_folders
		self.username, self.password, = username, password
		self.full_path = full_path
		kwargs['max_length'] = kwargs.get('max_length', 100)
		models.fields.Field.__init__(self, verbose_name, name, **kwargs)

	def formfield(self, **kwargs):
		defaults = {
				'path': self.path,
				'match': self.match,
				'recursive': self.recursive,
				'form_class': SVNFilePathFormField,
				'allow_files': self.allow_files,
				'allow_folders': self.allow_folders,
				'username': self.username,
				'password': self.password,
				'full_path': self.full_path,
			}
		defaults.update(kwargs)
		return super(SVNFilePathField, self).formfield(**defaults)

	def get_internal_type(self):
		return "CharField"

class SVNFilePathFormField(fields.ChoiceField):
	def __init__(self, path, match=None, recursive=False, allow_files=True,
			allow_folders=False, username='', password='', full_path=False,
			required=True, widget=None, label=None, initial=None, 
			help_text=None, *args, **kwargs):

		self.path, self.match, self.recursive = path, match, recursive
		self.allow_files, self.allow_folders = allow_files, allow_folders
		self.username, self.password = username, password
		self.full_path = full_path

		super(SVNFilePathFormField, self).__init__(choices=(), 
					required=required, widget=widget, label=label, 
					initial=initial, help_text=help_text, *args, **kwargs)

		if self.required:
			self.choices = []
		else:
			self.choices = [("","----------")]
		
		if self.match is not None:
			self.match_re = re.compile(self.match)
		
		if self.recursive:
			depth = pysvn.depth.infinity
		elif self.allow_folders:
			depth = pysvn.depth.immediates
		elif self.allow_files:
			depth = pysvn.depth.files
		else:
			depth = pysvn.depth.empty

		svn_client = pysvn.Client()
		def ssl_server_trust_prompt(trust_dict):
			return True, sys.maxint, False

		def get_login(realm, username, may_save):
			return True, self.username, self.password, False

		svn_client.callback_ssl_server_trust_prompt = ssl_server_trust_prompt
		svn_client.callback_get_login = get_login
		try:
			svn_response = [f[0] for f in svn_client.list(self.path, depth=depth)[1:]]
		except pysvn.ClientError:
			pass
		for f in svn_response:
			if self.full_path:
				value = f.repos_path
			else:
				value = os.path.basename(f.repos_path)
			if (((f.kind == pysvn.node_kind.file and self.allow_files) or
			(f.kind == pysvn.node_kind.dir and self.allow_folders)) and
			(self.match is None or self.match_re.search(f.repos_path))):
				self.choices.append((value,os.path.basename(f.repos_path)))

