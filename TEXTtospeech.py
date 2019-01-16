import pyttsx3;
engine = pyttsx3.init();
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say("Are you okay");
engine.runAndWait();



