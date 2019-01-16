import pyttsx3;
engine = pyttsx3.init();
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say("Can you her my voice?");
engine.runAndWait();



