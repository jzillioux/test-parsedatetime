import json
import datetime
import parsedatetime

DATE_FORMAT = '%m-%d-%y %I:%M %p'

def main():
    sample_file = 'samples.json'
    with open(sample_file, 'r') as f:
        sample_phrases = json.load(f)

    cal = parsedatetime.Calendar()

    print('=' * 20)
    for phrase in sample_phrases:
        ts, _ = cal.parse(phrase['text'])
        dt = datetime.datetime(*ts[:6])
        print('Phrase: {0:s} -> {1:s}'.format(phrase['text'], dt.strftime(DATE_FORMAT)))
    
    print('=' * 20)


if __name__ == '__main__':
    main()
