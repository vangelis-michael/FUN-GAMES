# Using Google Colab Research.
# You can use your local machine though.
from google.colab import files
uploaded = files.upload()

# Save the uploaded csv, xlsx or json file containing the words to wordcloud
for name, data in uploaded.items():
  with open(name, 'wb') as f:
    f.write(data)
    print ('saved file', name)

# List the directory    
ls

# Install wordcloud library 
!pip install wordcloud

# Import pandas since its a dataframe we are working with
import pandas as pd
purpose = pd.read_csv('purpose4.csv')

# View the first five words
purpose.head()

# Import some useful libraries
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# iterate through the csv file
for val in purpose.PurposeOfLoan:
     
    # typecaste each val to string
    val = str(val)
 
    # split the value
    tokens = val.split()
     
    # Converts each token into lowercase
    for i in range(len(tokens)):
      tokens[i] = tokens[i].lower()
         
    for words in tokens:
      comment_words = comment_words + words + ' '
 
# Adjust wordcloud dimensions as you please.
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='black',
                stopwords = stopwords,
                min_font_size = 10).generate(comment_words)
                
# plot the WordCloud image                       
fig = plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
 
plt.show()

# Save the figure
fig.savefig('majorwords3.jpeg')

# Download the file as an image
from google.colab import files
files.download('majorwords3.jpeg')
