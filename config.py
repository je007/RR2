import ConfigParser
import os

class ConfigError (ValueError):
	pass

class RRcfgParser(ConfigParser.ConfigParser): 
	def getlist(self, section, option):
		ret = []
		x = self.get(section, option) # Cuts up the user.cfg file into bits
		if x != None and x != "": # if x is nothing, or unset:
			for i in x.split(","):
				ret.append(i.strip())
		else:
			return []
		return ret
		
		
	def getpath(self, section, option):
		x = self.get(section, option)
		#print x
		if x != None and x.strip() != "": # splits file x up into 'snippets'?
			return os.path.join(*x.split())
		else:
			raise ConfigError, "Path wanted but not given: Section %s, option %s" % (section, option)

parser = RRcfgParser()

parser.read(os.path.join("data", "config", "main.cfg"))

extralist = parser.getlist("main", "includes");

for i in extralist:
	parser.read(os.path.join("data", "config", i))

