import json
import praw
import re
import sys
import traceback


class Bot():
    def __init__(self):
        self.settings = self.load_json('config.json')
        self.reddit   = self.reddit_instance(self.settings)

    def botcode(self):
        for submission in self.reddit.subreddit(self.settings['subreddit']).stream.submissions(skip_existing=True):
            if not self.needs_newlines(submission):
                continue

            response = self.build_submission_response(submission)
            submission.reply(response)

    def build_submission_response(self, submission):
        if self.settings['response_header'] == '':
            header = ''
        else:
            header = self.settings['response_header'] + '\n\n'

        return header + self.add_newlines(submission)

    def add_newlines(self, submission):
        body_lst = self.split_body(submission.selftext)
        chunked_body = self.chunk_sentences(body_lst)

        return '\n\n'.join(chunked_body)

    def chunk_sentences(self, lst):
        n = self.settings['sentence_threshold']

        return [' '.join(lst[i:i + n]) for i in range(0, len(lst), n)]

    def concatenate_minimum_sentences(self, lst):
        result = []

        for sentence in lst:
            if len(result) == 0:
                result.append(sentence)
                continue

            if len(sentence) < self.settings['minimum_sentence_length']:
                result[-1] = result[-1] + ' ' + sentence
            else:
                result.append(sentence)

        return result

    def split_body(self, body):
        split_body = re.split(r'(?<=[\.\?\!])\s', body)

        return self.concatenate_minimum_sentences(split_body)

    def needs_newlines(self, submission):
        if '\n\n' in submission.selftext or not submission.is_self:
            return False

        if len(self.split_body(submission.selftext)) > self.settings['sentence_threshold']:
            return True

        return False

    def reddit_instance(self, account_details):
        reddit = praw.Reddit(username=account_details['bot_username'],
                             password=account_details['bot_password'],
                             client_id=account_details['bot_client_id'],
                             client_secret=account_details['bot_client_secret'],
                             user_agent=account_details['bot_user_agent'])

        return reddit

    def load_json(self, path):
        with open(path) as f:
            data = json.load(f)

        return data


if __name__ == '__main__':
    while True:
        try:
            Bot().botcode()
        except KeyboardInterrupt:
            sys.exit(0)
        except Exception:
            traceback.print_exc()