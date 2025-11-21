"""
Symulator botow internetowych (w celach edukacyjnych!).
UWAGA: Ten kod ma EKSPLOZJE KLAS! Uzyj wzorca Bridge.

Mamy 4 typy botow i 4 platformy = 16 klas.
Dodanie nowej platformy wymaga 4 nowych klas!
Dodanie nowego bota wymaga 4 nowych klas!

To nie jest skalowalne rozwiazanie...
"""
from typing import Dict
import random

from abc import ABC, abstractmethod

# Implementacja (JAK formatuje)
class Platform(ABC):
	@abstractmethod
	def format_message(self, message: str) -> str:
		pass

class Facebook(Platform):
	def format_message(self, message: str) -> str:

		formatted = f"🔴 PILNE 🔴\n\n"
		formatted += f"{message}... PROSZE SIE OBUDZIC LUDZIE!!! "
		formatted += "Udostepnij zanim USUNĄ!!! "
		formatted += "😠😠😠"
		formatted += "NapiszINFO w komentarzu!!! 💰💰💰"
		formatted += f"UDOSTEPNIJ ZANIM USUNA!!!\n\n"
		formatted += "Zrobie researcha!!! 👁️👁️👁️"
		formatted += "Mainstream media UKRYWA to przed Toba!!! "
		formatted += "Media MILCZA! Udostepnij swoim znajomym!!! "
		formatted += "Twoja rodzina MUSI to zobaczyc!!! ⚠️⚠️⚠️"

		return formatted

class LinkedIn(Platform):
	def format_message(self, message: str) -> str:
		formatted = f"🚨 Industry Alert 🚨\n\n"
		formatted += f"Unpopular opinion: {message}\n\n"
		formatted += "I know this might be controversial, but someone had to say it.\n\n"
		formatted += "Agree? ♻️ Repost to spread awareness\n"
		formatted += f"I'm excited to announce that {message}\n\n"
		formatted += "This is not financial advice, but my portfolio is up 10000%.\n\n"
		formatted += "DM me for exclusive insights.\n"
		formatted += f"After 15 years in the industry, I need to share something:\n\n"
		formatted += "The elites don't want you to know this.\n\n"
		formatted += "Comment 'TRUTH' if you're awake.\n"
		formatted += "My sources in the industry have confirmed this.\n\n"
		formatted += "Share with your network before it's too late.\n"
		formatted += "#ThoughtLeadership #Disruption #Controversial"
		formatted += "#Entrepreneurship #Hustle #Blessed"
		formatted += "#DeepState #FollowTheMoney #QuestionEverything"
		formatted += "#BreakingNews #IndustryInsider #MustRead"
		return formatted

class TikTok(Platform):
	def format_message(self, message: str) -> str:
		formatted = f"pov: ktos mowi ze to ma sens 💀💀💀\n"
		formatted += f"bestie... {message}\n"
		formatted += "its giving delulu 😭 no cap fr fr"
		formatted += f"ok but why is nobody talking about this?? 🤑\n"
		formatted += f"{message}\n"
		formatted += "link in bio bestie trust me im just like you 💅"
		formatted += f"wait wait wait... 🤯\n"
		formatted += f"{message}\n"
		formatted += "why is this not on the news?? theyre deleting this video in 3...2... 👁️"
		formatted += f"STORYTIME: so i just found out something crazy 😱\n"
		formatted += f"{message}\n"
		formatted += "share before they take this down!! part 2 if this blows up 👀"
		return formatted

class Twitter(Platform):
	def format_message(self, message: str) -> str:
		formatted = f"🧵⚠️ WATEK: #triggered 🚀🚀🚀 {message} Link in bio!"
		if len(formatted) > 280:
			formatted = formatted[:277] + "..."

		return formatted

# Abstrakcja (CO generuje)
class Bot(ABC):
	def __init__(self, platform: Platform):
		self.platform = platform  # <-- TO JEST MOST!
	
	@abstractmethod
	def generate_content(self, topic: str) -> str:
		pass
	
	def generate_post(self, topic: str) -> str:
		content = self.generate_content(topic)
		formatted = self.platform.format_message(content)
		return formatted


class Troll(Bot):
	def generate_content(self, topic: str) -> str:
		provocations = [
			f"Serio wierzysz w {topic}?",
			f"{topic} to najwiekszy przekret w historii",
			f"Kazdy kto popiera {topic} nie ma pojecia o czyms"
		]
		content = random.choice(provocations)
		return content

class Spammer(Bot):
	def generate_content(self, topic: str) -> str:
		spam_templates = [
			f"NOWY {topic} COIN! 1000x gwarantowane!",
			f"Zarobiles na {topic}? JA TAK! Sprawdz jak",
			f"{topic} MOON SOON! Ostatnia szansa!"
		]
		content = random.choice(spam_templates)
		return content

class Conspiracist(Bot):
	def generate_content(self, topic: str) -> str:
		conspiracies = [
			f"Czy zastanawiales sie KOMU zalezy na {topic}?",
			f"{topic} to przykrywka dla PRAWDZIWEGO planu",
			f"Oni nie chca zebys wiedzial prawde o {topic}"
		]
		content = random.choice(conspiracies)
		return content

class FakeNews(Bot):
	def generate_content(self, topic: str) -> str:
		fake_news = [
			f"BREAKING: Naukowcy potwierdzili ze {topic} jest niebezpieczne",
			f"PILNE: Rzad ukrywa prawde o {topic}",
			f"SZOK: Ekspert ujawnia co NAPRAWDE kryje sie za {topic}"
		]
		content = random.choice(fake_news)
		return content

# ============================================================================
# TROLL BOTY - prowokuja klocnie na roznych platformach
# ============================================================================

class TrollTwitterBot:
	"""Troll na Twitterze - krotki, agresywny"""
	
	def __init__(self):
		self.bot_type = "Troll"
		self.platform = "Twitter"
	
	def generate_post(self, topic: str) -> Dict:
		formatted = Troll(Twitter()).generate_post(topic)
		
		return {
			"bot_type": self.bot_type,
			"platform": self.platform,
			"topic": topic,
			"content": formatted
		}


class TrollFacebookBot:
	"""Troll na Facebooku - boomerski styl"""
	
	def __init__(self):
		self.bot_type = "Troll"
		self.platform = "Facebook"
	
	def generate_post(self, topic: str) -> Dict:
		formatted = Troll(Facebook()).generate_post(topic)
		
		return {
			"bot_type": self.bot_type,
			"platform": self.platform,
			"topic": topic,
			"content": formatted
		}


class TrollLinkedInBot:
	"""Troll na LinkedIn - korporacyjna prowokacja"""
	
	def __init__(self):
		self.bot_type = "Troll"
		self.platform = "LinkedIn"
	
	def generate_post(self, topic: str) -> Dict:
		formatted = Troll(LinkedIn()).generate_post(topic)
		
		return {
			"bot_type": self.bot_type,
			"platform": self.platform,
			"topic": topic,
			"content": formatted
		}


class TrollTikTokBot:
	"""Troll na TikToku - GenZ styl"""
	
	def __init__(self):
		self.bot_type = "Troll"
		self.platform = "TikTok"
	
	def generate_post(self, topic: str) -> Dict:
		formatted = Troll(TikTok()).generate_post(topic)
		
		return {
			"bot_type": self.bot_type,
			"platform": self.platform,
			"topic": topic,
			"content": formatted
		}


# ============================================================================
# SPAMMER BOTY - promuja podejrzane produkty/krypto
# ============================================================================

class SpammerTwitterBot:
	"""Spammer na Twitterze"""
	
	def __init__(self):
		self.bot_type = "Spammer"
		self.platform = "Twitter"
	
	def generate_post(self, topic: str) -> Dict:
		formatted = Spammer(Twitter()).generate_post(topic)
		
		return {
			"bot_type": self.bot_type,
			"platform": self.platform,
			"topic": topic,
			"content": formatted
		}


class SpammerFacebookBot:
	"""Spammer na Facebooku"""
	
	def __init__(self):
		self.bot_type = "Spammer"
		self.platform = "Facebook"
	
	def generate_post(self, topic: str) -> Dict:
		formatted = Spammer(Facebook()).generate_post(topic)
		
		# Facebook formatowanie
		
		return {
			"bot_type": self.bot_type,
			"platform": self.platform,
			"topic": topic,
			"content": formatted
		}


class SpammerLinkedInBot:
	"""Spammer na LinkedIn"""
	
	def __init__(self):
		self.bot_type = "Spammer"
		self.platform = "LinkedIn"
	
	def generate_post(self, topic: str) -> Dict:
		formatted = Spammer(LinkedIn()).generate_post(topic)
		
		return {
			"bot_type": self.bot_type,
			"platform": self.platform,
			"topic": topic,
			"content": formatted
		}


class SpammerTikTokBot:
	"""Spammer na TikToku"""
	
	def __init__(self):
		self.bot_type = "Spammer"
		self.platform = "TikTok"
	
	def generate_post(self, topic: str) -> Dict:
		formatted = Spammer(TikTok()).generate_post(topic)
		
		return {
			"bot_type": self.bot_type,
			"platform": self.platform,
			"topic": topic,
			"content": formatted
		}


# ============================================================================
# CONSPIRACIST BOTY - wszedzie widza spiski
# ============================================================================

class ConspiracistTwitterBot:
	"""Conspiracist na Twitterze"""
	
	def __init__(self):
		self.bot_type = "Conspiracist"
		self.platform = "Twitter"
	
	def generate_post(self, topic: str) -> Dict:
		formatted = Conspiracist(Twitter()).generate_post(topic)
		
		return {
			"bot_type": self.bot_type,
			"platform": self.platform,
			"topic": topic,
			"content": formatted
		}


class ConspiracistFacebookBot:
	"""Conspiracist na Facebooku"""
	
	def __init__(self):
		self.bot_type = "Conspiracist"
		self.platform = "Facebook"
	
	def generate_post(self, topic: str) -> Dict:
		formatted = Conspiracist(Facebook()).generate_post(topic)
		
		return {
			"bot_type": self.bot_type,
			"platform": self.platform,
			"topic": topic,
			"content": formatted
		}


class ConspiracistLinkedInBot:
	"""Conspiracist na LinkedIn"""
	
	def __init__(self):
		self.bot_type = "Conspiracist"
		self.platform = "LinkedIn"
	
	def generate_post(self, topic: str) -> Dict:
		formatted = Conspiracist(LinkedIn()).generate_post(topic)
		
		return {
			"bot_type": self.bot_type,
			"platform": self.platform,
			"topic": topic,
			"content": formatted
		}


class ConspiracistTikTokBot:
	"""Conspiracist na TikToku"""
	
	def __init__(self):
		self.bot_type = "Conspiracist"
		self.platform = "TikTok"
	
	def generate_post(self, topic: str) -> Dict:
		formatted = Conspiracist(TikTok()).generate_post(topic)
		
		return {
			"bot_type": self.bot_type,
			"platform": self.platform,
			"topic": topic,
			"content": formatted
		}


# ============================================================================
# FAKENEWS BOTY - szerza dezinformacje
# ============================================================================

class FakeNewsTwitterBot:
	"""FakeNews na Twitterze"""
	
	def __init__(self):
		self.bot_type = "FakeNews"
		self.platform = "Twitter"
	
	def generate_post(self, topic: str) -> Dict:
		formatted = FakeNews(Twitter()).generate_post(topic)
		
		return {
			"bot_type": self.bot_type,
			"platform": self.platform,
			"topic": topic,
			"content": formatted
		}


class FakeNewsFacebookBot:
	"""FakeNews na Facebooku"""
	
	def __init__(self):
		self.bot_type = "FakeNews"
		self.platform = "Facebook"
	
	def generate_post(self, topic: str) -> Dict:
		formatted = FakeNews(Facebook()).generate_post(topic)
		
		return {
			"bot_type": self.bot_type,
			"platform": self.platform,
			"topic": topic,
			"content": formatted
		}


class FakeNewsLinkedInBot:
	"""FakeNews na LinkedIn"""
	
	def __init__(self):
		self.bot_type = "FakeNews"
		self.platform = "LinkedIn"
	
	def generate_post(self, topic: str) -> Dict:
		formatted = FakeNews(LinkedIn()).generate_post(topic)
		
		return {
			"bot_type": self.bot_type,
			"platform": self.platform,
			"topic": topic,
			"content": formatted
		}


class FakeNewsTikTokBot:
	"""FakeNews na TikToku"""
	
	def __init__(self):
		self.bot_type = "FakeNews"
		self.platform = "TikTok"
	
	def generate_post(self, topic: str) -> Dict:
		formatted = FakeNews(TikTok()).generate_post(topic)
		
		return {
			"bot_type": self.bot_type,
			"platform": self.platform,
			"topic": topic,
			"content": formatted
		}


# ============================================================================
# FUNKCJA POMOCNICZA
# ============================================================================

def get_bot(bot_type: str, platform: str):
	"""
	Zwraca odpowiedniego bota dla danego typu i platformy.
	
	SPÓJRZ NA TE IFY! 16 kombinacji! A co jak dodamy Mastodon i Reddit?
	"""
	if bot_type == "Troll":
		if platform == "Twitter":
			return TrollTwitterBot()
		elif platform == "Facebook":
			return TrollFacebookBot()
		elif platform == "LinkedIn":
			return TrollLinkedInBot()
		elif platform == "TikTok":
			return TrollTikTokBot()
	elif bot_type == "Spammer":
		if platform == "Twitter":
			return SpammerTwitterBot()
		elif platform == "Facebook":
			return SpammerFacebookBot()
		elif platform == "LinkedIn":
			return SpammerLinkedInBot()
		elif platform == "TikTok":
			return SpammerTikTokBot()
	elif bot_type == "Conspiracist":
		if platform == "Twitter":
			return ConspiracistTwitterBot()
		elif platform == "Facebook":
			return ConspiracistFacebookBot()
		elif platform == "LinkedIn":
			return ConspiracistLinkedInBot()
		elif platform == "TikTok":
			return ConspiracistTikTokBot()
	elif bot_type == "FakeNews":
		if platform == "Twitter":
			return FakeNewsTwitterBot()
		elif platform == "Facebook":
			return FakeNewsFacebookBot()
		elif platform == "LinkedIn":
			return FakeNewsLinkedInBot()
		elif platform == "TikTok":
			return FakeNewsTikTokBot()
	
	raise ValueError(f"Unknown bot_type '{bot_type}' or platform '{platform}'")


# Przykladowe uzycie
if __name__ == "__main__":
	print("=" * 60)
	print("SYMULATOR BOTOW INTERNETOWYCH")
	print("(w celach edukacyjnych!)")
	print("=" * 60)
	
	# Ustawmy seed dla powtarzalnosci
	random.seed(42)
	
	bot_types = ["Troll", "Spammer", "Conspiracist", "FakeNews"]
	platforms = ["Twitter", "Facebook", "LinkedIn", "TikTok"]
	topics = ["AI", "szczepionki", "5G", "kryptowaluty"]
	
	for bot_type in bot_types:
		print(f"\n{'='*60}")
		print(f"TYP BOTA: {bot_type}")
		print("=" * 60)
		
		for platform in platforms:
			bot = get_bot(bot_type, platform)
			topic = random.choice(topics)
			result = bot.generate_post(topic)
			
			print(f"\n[{platform}] Temat: {topic}")
			print("-" * 40)
			print(result["content"])
