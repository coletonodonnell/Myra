import sqlite3

def create_table():
    conn = sqlite3.connect('services/voices.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Voice (
                    Name TEXT,
                    VoiceID TEXT PRIMARY KEY,
                    Stability REAL,
                    Similarity REAL,
                    Style REAL,
                    SpeakerBoost BOOLEAN
                )''')
    conn.commit()
    conn.close()

def store_voice(name, voice_id, stability, similarity, style, speaker_boost):
    conn = sqlite3.connect('services/voices.db')
    c = conn.cursor()
    c.execute('''INSERT INTO Voice (Name, VoiceID, Stability, Similarity, Style, SpeakerBoost)
                 VALUES (?, ?, ?, ?, ?, ?)''', (name, voice_id, stability, similarity, style, speaker_boost))
    conn.commit()
    conn.close()

def delete_voice(voice_id):
    conn = sqlite3.connect('services/voices.db')
    c = conn.cursor()
    c.execute('''DELETE FROM Voice WHERE VoiceID = ?''', (voice_id,))
    conn.commit()
    conn.close()

def retrieve_voice(voice_id):
    conn = sqlite3.connect('services/voices.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM Voice WHERE VoiceID = ?''', (voice_id,))
    voice = c.fetchone()
    conn.close()
    return voice

def get_all_voices():
    conn = sqlite3.connect('services/voices.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM Voice''')
    voices = c.fetchall()
    conn.close()
    return voices

def voice_exists(voice_id):
    conn = sqlite3.connect('services/voices.db')
    c = conn.cursor()
    c.execute('''SELECT 1 FROM Voice WHERE VoiceID = ?''', (voice_id,))
    exists = c.fetchone() is not None
    conn.close()
    return exists

# Initialize the database table
create_table()