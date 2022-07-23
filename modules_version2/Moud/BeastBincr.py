from pbwrap import Pastebin
class BCR:
	def bastbincr(self, key , username , Password , data):
		pb = Pastebin(key)
		pb.authenticate(username,Password)
		self.x = pb.create_paste(str(data),
			api_paste_private=2,
			api_paste_name="None", 
			api_paste_expire_date=None, 
			api_paste_format=None) 
