from textblob import TextBlob
from elasticsearch import Elasticsearch

es = Elasticsearch()

test_inputs = [ 'sushi', 'bread', 'fish', 'coffee']

for test in test_inputs:

	search_query =  {'query' : 
						{'term' : 
							{'text' : test}
						}
					}

	results = es.search(index='pregnancy', body=search_query)

	count = results['hits']['total']

	if count > 0:

		# seems like hits are sorted by score so getting first one seems to be fine
		top_hit = results['hits']['hits'][0]

		hit_id = top_hit['_id']
		source = top_hit['_source']['source']
		text = top_hit['_source']['text']

		# if you need to delete
		# es.delete(index='pregnancy', doc_type='html', id='nstUualoRFWaTO-F8pkmNg')

		# print(hit_id)
		# print(source)
		# print(text)

		b = TextBlob(text)

		# sentiment - focusing on polarity expressed in a range from -1.0 - 1.0
		sentiment = b.sentiment[0]

		if (sentiment >= 0):
			print("%s is safe to eat" % test)
		else:
			print("%s is not safe to eat" % test)