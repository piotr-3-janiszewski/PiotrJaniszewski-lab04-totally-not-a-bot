"""
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
	platform = "Facebook"
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
	platform = "LinkedIn"
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
	platform = "TikTok"
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
	platform = "Twitter"
	def format_message(self, message: str) -> str:
		formatted = f"🧵⚠️ WATEK: #triggered 🚀🚀🚀 {message} Link in bio!"
		if len(formatted) > 280:
			formatted = formatted[:277] + "..."

		return formatted

# Abstrakcja (CO generuje)
class Bot(ABC):
	def __init__(self, platform: Platform):
		self.platformObject = platform  # <-- TO JEST MOST!
		self.platform = platform.platform
	
	@abstractmethod
	def generate_content(self, topic: str) -> str:
		pass
	
	def generate_post(self, topic: str) -> str:
		content = self.generate_content(topic)
		formatted = self.platformObject.format_message(content)

		return {
			"bot_type": self.bot_type,
			"platform": self.platform,
			"topic": topic,
			"content": formatted
		}


class Troll(Bot):
	bot_type = "Troll"
	def generate_content(self, topic: str) -> str:
		provocations = [
			f"Serio wierzysz w {topic}?",
			f"{topic} to najwiekszy przekret w historii",
			f"Kazdy kto popiera {topic} nie ma pojecia o czyms"
		]
		content = random.choice(provocations)
		return content

class Spammer(Bot):
	bot_type = "Spammer"
	def generate_content(self, topic: str) -> str:
		spam_templates = [
			f"NOWY {topic} COIN! 1000x gwarantowane!",
			f"Zarobiles na {topic}? JA TAK! Sprawdz jak",
			f"{topic} MOON SOON! Ostatnia szansa!"
		]
		content = random.choice(spam_templates)
		return content

class Conspiracist(Bot):
	bot_type = "Conspiracist"
	def generate_content(self, topic: str) -> str:
		conspiracies = [
			f"Czy zastanawiales sie KOMU zalezy na {topic}?",
			f"{topic} to przykrywka dla PRAWDZIWEGO planu",
			f"Oni nie chca zebys wiedzial prawde o {topic}"
		]
		content = random.choice(conspiracies)
		return content

class FakeNews(Bot):
	bot_type = "FakeNews"
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

def create_bot_adapter(bot_class, platform_class):
	"""Factory Method - generuje klase adaptera"""
	class BotAdapter:
		def generate_post(self, topic):
			return self._bot.generate_post(topic)
			
		def __init__(self):
			self._bot = bot_class(platform_class())
			self.bot_type = self._bot.bot_type
			self.platform = self._bot.platform
		
	return BotAdapter  # Zwraca KLASE, nie obiekt!

bot_types = {
	"Troll": Troll,
	"Spammer": Spammer,
	"Conspiracist": Conspiracist,
	"FakeNews": FakeNews
}

platforms = {
	"Twitter": Twitter,
	"Facebook": Facebook,
	"LinkedIn": LinkedIn,
	"TikTok": TikTok
}

# Magia!
for bot_name, bot_class in bot_types.items():
	for platform_name, platform_class in platforms.items():
		class_name = f"{bot_name}{platform_name}Bot"
		globals()[class_name] = create_bot_adapter(bot_class, platform_class)

def magic(bot, platform):
	return f"{bot}{platform}Bot"

import sys 
def get_bot(bot, platform):
	if (magic(bot,platform) in globals()):
		return globals()[magic(bot, platform)]()
	else:
		raise ValueError("masło")

