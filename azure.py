import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import textwrap
from gtts import gTTS
import os

#file_path = '/content/તલાટી અને જુનિયર કલાર્ક મોડેલ પેપર -2 - તલાટી અને જુનિયર કલાર્ક મોડેલ પેપર -2(1).csv'
#data_frame = pd.read_csv(file_path)
#data_list = data_frame.values.tolist()

# data_list = [["કલકત્તામાં એશિયાટિક સોસાયટીની સ્થાપના સમયે બંગાળના ગવર્નર જનરલ કોણ હતા ?", "A. કોનૅવોલીસ", "B. વિલિયમ બેન્ટિક", "C. વોરન હેસ્ટીંગ્સ", "D. વેલેસ્લી", "જવાબ :- વોરન હેસ્ટીંગ્સ", ""],
#     ["સ્વામી વિવેકાનંદ નું મૂળ નામ શું હતું ?", "A. સુરેન્દ્રનાથ", "B. રવીન્દ્રનાથ", "C. રામકૃષ્ણ", "D. નરેન્દ્રનાથ", "જવાબ  નરેન્દ્રનાથ", ""]]
data_list = [
       ["What is the primary goal of artificial intelligence in the context of business applications?", 
    "A. Automating repetitive tasks", 
    "B. Enhancing human decision-making", 
    "C. Personalizing user experiences", 
    "D. All of the above", 
    "Answer: D. All of the above", ""],
    
    ["Which AI workload focuses on understanding and generating human language?", 
    "A. Computer Vision", 
    "B. Natural Language Processing (NLP)", 
    "C. Knowledge Mining", 
    "D. Content Moderation", 
    "Answer: B. Natural Language Processing (NLP)", ""],
    
    ["What is the main feature of content moderation workloads in AI?", 
    "A. Classifying images", 
    "B. Detecting inappropriate content", 
    "C. Translating languages", 
    "D. Generating text", 
    "Answer: B. Detecting inappropriate content", ""],
    
    ["Which type of AI workload is used to analyze and extract information from images and videos?", 
    "A. Natural Language Processing (NLP)", 
    "B. Generative AI", 
    "C. Computer Vision", 
    "D. Knowledge Mining", 
    "Answer: C. Computer Vision", ""],
    
    ["What is a common application of personalization workloads in AI?", 
    "A. Recommending products to users", 
    "B. Translating text", 
    "C. Moderating content", 
    "D. Analyzing documents", 
    "Answer: A. Recommending products to users", ""],
    
    ["Which AI workload involves extracting structured information from unstructured data sources?", 
    "A. Content Moderation", 
    "B. Document Intelligence", 
    "C. Computer Vision", 
    "D. Knowledge Mining", 
    "Answer: D. Knowledge Mining", ""],
    
    ["What is the focus of document intelligence workloads in AI?", 
    "A. Creating new documents", 
    "B. Understanding and processing existing documents", 
    "C. Moderating text content", 
    "D. Translating documents", 
    "Answer: B. Understanding and processing existing documents", ""],
    
    ["Which feature is associated with generative AI workloads?", 
    "A. Creating new and unique content", 
    "B. Translating languages", 
    "C. Analyzing images", 
    "D. Extracting key information from text", 
    "Answer: A. Creating new and unique content", ""],
    
    ["What is a key consideration when implementing AI for content moderation?", 
    "A. Ensuring high accuracy in detecting inappropriate content", 
    "B. Automating language translation", 
    "C. Personalizing recommendations", 
    "D. Extracting information from documents", 
    "Answer: A. Ensuring high accuracy in detecting inappropriate content", ""],
    
    ["What type of AI workload is used for summarizing large volumes of text?", 
    "A. Natural Language Processing (NLP)", 
    "B. Computer Vision", 
    "C. Document Intelligence", 
    "D. Generative AI", 
    "Answer: C. Document Intelligence", ""],["What is a key principle of responsible AI?", 
    "A. Maximizing profit", 
    "B. Ensuring fairness and equity", 
    "C. Reducing computational cost", 
    "D. Accelerating deployment", 
    "Answer: B. Ensuring fairness and equity", ""],
    
    ["Which consideration ensures that AI solutions do not discriminate against certain groups?", 
    "A. Transparency", 
    "B. Privacy", 
    "C. Fairness", 
    "D. Accountability", 
    "Answer: C. Fairness", ""],
    
    ["What is a critical aspect of ensuring AI reliability and safety?", 
    "A. Frequent updates", 
    "B. Rigorous testing and validation", 
    "C. Minimizing costs", 
    "D. Maximizing data collection", 
    "Answer: B. Rigorous testing and validation", ""],
    
    ["Which principle involves protecting user data from unauthorized access?", 
    "A. Fairness", 
    "B. Inclusiveness", 
    "C. Privacy and Security", 
    "D. Transparency", 
    "Answer: C. Privacy and Security", ""],
    
    ["Why is inclusiveness important in AI solutions?", 
    "A. To ensure the solution works for all user groups", 
    "B. To reduce development time", 
    "C. To minimize resource usage", 
    "D. To comply with regulations", 
    "Answer: A. To ensure the solution works for all user groups", ""],
    
    ["What does transparency in AI solutions involve?", 
    "A. Hiding the AI algorithms used", 
    "B. Clearly explaining how AI decisions are made", 
    "C. Limiting user access to information", 
    "D. Increasing data collection", 
    "Answer: B. Clearly explaining how AI decisions are made", ""],
    
    ["Which consideration focuses on who is responsible for the outcomes of AI systems?", 
    "A. Accountability", 
    "B. Inclusiveness", 
    "C. Fairness", 
    "D. Privacy", 
    "Answer: A. Accountability", ""],
    
    ["What is a primary goal of incorporating fairness into AI?", 
    "A. Improving speed", 
    "B. Reducing bias", 
    "C. Increasing profitability", 
    "D. Enhancing user experience", 
    "Answer: B. Reducing bias", ""],
    
    ["How can AI developers ensure the reliability of their solutions?", 
    "A. By continuously monitoring performance and outcomes", 
    "B. By minimizing computational power", 
    "C. By using only proprietary data", 
    "D. By avoiding user feedback", 
    "Answer: A. By continuously monitoring performance and outcomes", ""],
    
    ["Why is accountability important in AI systems?", 
    "A. It ensures that there is a clear chain of responsibility for AI actions", 
    "B. It reduces the need for testing", 
    "C. It increases system complexity", 
    "D. It maximizes data usage", 
    "Answer: A. It ensures that there is a clear chain of responsibility for AI actions", ""], ["Which machine learning technique is used for predicting continuous values?", 
    "A. Classification", 
    "B. Regression", 
    "C. Clustering", 
    "D. Reinforcement Learning", 
    "Answer: B. Regression", ""],
    
    ["What is the goal of classification in machine learning?", 
    "A. To group data points into clusters", 
    "B. To predict continuous outcomes", 
    "C. To assign data points to predefined categories", 
    "D. To generate new data", 
    "Answer: C. To assign data points to predefined categories", ""],
    
    ["Which scenario is best suited for clustering techniques?", 
    "A. Predicting house prices", 
    "B. Diagnosing diseases", 
    "C. Customer segmentation", 
    "D. Classifying spam emails", 
    "Answer: C. Customer segmentation", ""],
    
    ["What is a key characteristic of deep learning techniques?", 
    "A. Use of decision trees", 
    "B. Layered neural networks", 
    "C. Simple linear models", 
    "D. K-means algorithm", 
    "Answer: B. Layered neural networks", ""],
    
    ["Which machine learning technique is typically used for anomaly detection?", 
    "A. Regression", 
    "B. Classification", 
    "C. Clustering", 
    "D. Deep Learning", 
    "Answer: C. Clustering", ""],
    
    ["What is a common application of regression techniques?", 
    "A. Image recognition", 
    "B. Predicting stock prices", 
    "C. Spam detection", 
    "D. Grouping customers", 
    "Answer: B. Predicting stock prices", ""],
    
    ["Which type of machine learning model is used to categorize emails as spam or not spam?", 
    "A. Regression", 
    "B. Classification", 
    "C. Clustering", 
    "D. Deep Learning", 
    "Answer: B. Classification", ""],
    
    ["What is an example of a deep learning application?", 
    "A. Linear regression for house price prediction", 
    "B. K-means clustering for market segmentation", 
    "C. Convolutional neural networks for image recognition", 
    "D. Decision tree for classification", 
    "Answer: C. Convolutional neural networks for image recognition", ""],
    
    ["Which technique would be used to group similar items without pre-labeled data?", 
    "A. Regression", 
    "B. Classification", 
    "C. Clustering", 
    "D. Deep Learning", 
    "Answer: C. Clustering", ""],
    
    ["What is a feature of supervised learning techniques?", 
    "A. No labeled data is used", 
    "B. Models are trained using labeled data", 
    "C. Models find hidden patterns in data without guidance", 
    "D. Models generate new data from scratch", 
    "Answer: B. Models are trained using labeled data", ""], ["What are features and labels in a machine learning dataset?", 
    "A. Features are the output variables, labels are the input variables", 
    "B. Features are the input variables, labels are the output variables", 
    "C. Features and labels are the same", 
    "D. Features and labels are not used in machine learning", 
    "Answer: B. Features are the input variables, labels are the output variables", ""],
    
    ["How are training and validation datasets typically used in machine learning?", 
    "A. Training dataset is used to evaluate model performance, validation dataset is used for model training", 
    "B. Training dataset is used for model training, validation dataset is used to evaluate model performance", 
    "C. Both datasets are used for model training", 
    "D. Both datasets are used to evaluate model performance", 
    "Answer: B. Training dataset is used for model training, validation dataset is used to evaluate model performance", ""],
    
    ["What are some capabilities of Azure Machine Learning?", 
    "A. Model training, deployment, and monitoring", 
    "B. Data visualization and exploration only", 
    "C. Cloud storage management", 
    "D. Database administration", 
    "Answer: A. Model training, deployment, and monitoring", ""],
    
    ["What are the capabilities of automated machine learning (AutoML)?", 
    "A. Automatic feature engineering, model selection, and hyperparameter tuning", 
    "B. Manual data preprocessing and model training", 
    "C. Visualization tools only", 
    "D. Cloud storage management", 
    "Answer: A. Automatic feature engineering, model selection, and hyperparameter tuning", ""],
    
    ["What are examples of data and compute services for data science and machine learning in Azure?", 
    "A. Azure Machine Learning, Azure Databricks, Azure Data Lake", 
    "B. Azure Virtual Machines, Azure SQL Database, Azure Cosmos DB", 
    "C. Azure Kubernetes Service, Azure Functions, Azure Logic Apps", 
    "D. Azure Storage, Azure DevOps, Azure Active Directory", 
    "Answer: A. Azure Machine Learning, Azure Databricks, Azure Data Lake", ""],
    
    ["What is the purpose of model management and deployment capabilities in Azure Machine Learning?", 
    "A. To automate data preprocessing", 
    "B. To visualize data", 
    "C. To deploy and manage machine learning models at scale", 
    "D. To monitor cloud infrastructure", 
    "Answer: C. To deploy and manage machine learning models at scale", ""],
    
    ["How are features and labels typically represented in a machine learning dataset?", 
    "A. Features are stored in rows, labels in columns", 
    "B. Features are stored in columns, labels in rows", 
    "C. Features and labels are stored in separate datasets", 
    "D. Features and labels are stored in the same column", 
    "Answer: B. Features are stored in columns, labels in rows", ""],
    
    ["What is the primary purpose of the validation dataset in machine learning?", 
    "A. To train the model", 
    "B. To evaluate the model's performance", 
    "C. To test the model's generalization ability", 
    "D. To preprocess the data", 
    "Answer: B. To evaluate the model's performance", ""],
    
    ["What are some advantages of using Azure Machine Learning for model deployment?", 
    "A. Scalability, monitoring, and version control", 
    "B. Data visualization and exploration", 
    "C. Cloud storage management", 
    "D. Database administration", 
    "Answer: A. Scalability, monitoring, and version control", ""],
    
    ["What is the purpose of automated machine learning (AutoML)?", 
    "A. To automate the entire machine learning process from data preprocessing to model deployment", 
    "B. To manually select features and labels", 
    "C. To visualize data only", 
    "D. To monitor cloud infrastructure", 
    "Answer: A. To automate the entire machine learning process from data preprocessing to model deployment", ""],
      ["What are some common types of computer vision solutions?", 
    "A. Image classification, object detection, optical character recognition", 
    "B. Data visualization, clustering, regression", 
    "C. Natural language processing, sentiment analysis, speech recognition", 
    "D. Cloud storage management, database administration, virtualization", 
    "Answer: A. Image classification, object detection, optical character recognition", ""],
    
    ["What are features typically associated with image classification solutions?", 
    "A. Identifying and categorizing objects within an image", 
    "B. Detecting and tracking objects in real-time", 
    "C. Converting handwritten or printed text into machine-readable text", 
    "D. Analyzing facial features and expressions", 
    "Answer: A. Identifying and categorizing objects within an image", ""],
    
    ["What are features commonly found in object detection solutions?", 
    "A. Assigning labels to images", 
    "B. Detecting and localizing multiple objects within an image", 
    "C. Recognizing handwritten or printed text", 
    "D. Analyzing facial features and expressions", 
    "Answer: B. Detecting and localizing multiple objects within an image", ""],
    
    ["What features are associated with optical character recognition (OCR) solutions?", 
    "A. Identifying and categorizing objects within an image", 
    "B. Detecting and localizing multiple objects within an image", 
    "C. Converting handwritten or printed text into machine-readable text", 
    "D. Analyzing facial features and expressions", 
    "Answer: C. Converting handwritten or printed text into machine-readable text", ""],
    
    ["What features are typically included in facial detection and facial analysis solutions?", 
    "A. Assigning labels to images", 
    "B. Detecting and tracking objects in real-time", 
    "C. Recognizing handwritten or printed text", 
    "D. Analyzing facial features and expressions", 
    "Answer: D. Analyzing facial features and expressions", ""],
    
    ["What is the primary goal of image classification solutions?", 
    "A. Detecting and tracking objects in real-time", 
    "B. Identifying and categorizing objects within an image", 
    "C. Converting handwritten or printed text into machine-readable text", 
    "D. Analyzing facial features and expressions", 
    "Answer: B. Identifying and categorizing objects within an image", ""],
    
    ["What is the main purpose of object detection solutions?", 
    "A. Assigning labels to images", 
    "B. Detecting and localizing multiple objects within an image", 
    "C. Recognizing handwritten or printed text", 
    "D. Analyzing facial features and expressions", 
    "Answer: B. Detecting and localizing multiple objects within an image", ""],
    
    ["Why are optical character recognition (OCR) solutions used?", 
    "A. To assign labels to images", 
    "B. To detect and track objects in real-time", 
    "C. To convert handwritten or printed text into machine-readable text", 
    "D. To analyze facial features and expressions", 
    "Answer: C. To convert handwritten or printed text into machine-readable text", ""],
    
    ["What is the primary function of facial detection and facial analysis solutions?", 
    "A. To assign labels to images", 
    "B. To detect and track objects in real-time", 
    "C. To recognize handwritten or printed text", 
    "D. To analyze facial features and expressions", 
    "Answer: D. To analyze facial features and expressions", ""],
    
    ["What are common applications of object detection solutions?", 
    "A. Medical image analysis, autonomous driving, security surveillance", 
    "B. Sentiment analysis, recommendation systems, fraud detection", 
    "C. Speech recognition, language translation, chatbots", 
    "D. Cloud storage management, database administration, virtualization", 
    "Answer: A. Medical image analysis, autonomous driving, security surveillance", ""],
     ["What are some Azure tools and services commonly used for computer vision tasks?", 
    "A. Azure Computer Vision, Azure Custom Vision, Azure Face API", 
    "B. Azure Machine Learning, Azure Databricks, Azure Data Lake", 
    "C. Azure Functions, Azure Logic Apps, Azure Kubernetes Service", 
    "D. Azure SQL Database, Azure Cosmos DB, Azure Storage", 
    "Answer: A. Azure Computer Vision, Azure Custom Vision, Azure Face API", ""],
    
    ["What are the capabilities of the Azure AI Vision service?", 
    "A. Recognizing and categorizing objects within images, extracting text from images, generating image descriptions", 
    "B. Analyzing sentiment from text data, translating languages, generating speech from text", 
    "C. Detecting anomalies in time-series data, predicting future outcomes, optimizing resource allocation", 
    "D. Automating data preprocessing, feature engineering, and model selection", 
    "Answer: A. Recognizing and categorizing objects within images, extracting text from images, generating image descriptions", ""],
    
    ["What are the capabilities of the Azure AI Face detection service?", 
    "A. Recognizing and categorizing objects within images, extracting text from images, generating image descriptions", 
    "B. Analyzing sentiment from text data, translating languages, generating speech from text", 
    "C. Detecting faces in images, identifying facial landmarks, estimating emotional expressions", 
    "D. Automating data preprocessing, feature engineering, and model selection", 
    "Answer: C. Detecting faces in images, identifying facial landmarks, estimating emotional expressions", ""],
    
    ["What is the primary function of the Azure AI Vision service?", 
    "A. Detecting faces in images", 
    "B. Recognizing and categorizing objects within images", 
    "C. Extracting text from images", 
    "D. Generating image descriptions", 
    "Answer: B. Recognizing and categorizing objects within images", ""],
    
    ["What task can the Azure AI Face detection service perform?", 
    "A. Analyzing sentiment from text data", 
    "B. Translating languages", 
    "C. Detecting faces in images", 
    "D. Generating speech from text", 
    "Answer: C. Detecting faces in images", ""],
    
    ["What type of tasks can the Azure AI Vision service help with?", 
    "A. Analyzing sentiment from text data", 
    "B. Translating languages", 
    "C. Recognizing and categorizing objects within images", 
    "D. Generating speech from text", 
    "Answer: C. Recognizing and categorizing objects within images", ""],
    
    ["What capability does the Azure AI Face detection service offer in addition to detecting faces?", 
    "A. Extracting text from images", 
    "B. Identifying facial landmarks", 
    "C. Analyzing sentiment from text data", 
    "D. Translating languages", 
    "Answer: B. Identifying facial landmarks", ""],
    
    ["What is a primary use case for the Azure AI Vision service?", 
    "A. Analyzing sentiment from text data", 
    "B. Detecting and tracking objects in real-time", 
    "C. Recognizing and categorizing objects within images", 
    "D. Translating languages", 
    "Answer: C. Recognizing and categorizing objects within images", ""],
    
    ["What is a key feature of the Azure AI Face detection service?", 
    "A. Recognizing and categorizing objects within images", 
    "B. Identifying facial landmarks and estimating emotional expressions", 
    "C. Extracting text from images", 
    "D. Generating image descriptions", 
    "Answer: B. Identifying facial landmarks and estimating emotional expressions", ""],
    
    ["What are some tasks that the Azure AI Face detection service can perform?", 
    "A. Analyzing sentiment from text data", 
    "B. Detecting faces in images, identifying facial landmarks, estimating emotional expressions", 
    "C. Recognizing and categorizing objects within images", 
    "D. Translating languages", 
    "Answer: B. Detecting faces in images, identifying facial landmarks, estimating emotional expressions", ""],
     ["What are some features of Natural Language Processing (NLP) workloads on Azure?", 
    "A. Text analytics, language understanding, text generation", 
    "B. Image classification, object detection, optical character recognition", 
    "C. Speech recognition, sentiment analysis, translation", 
    "D. Database administration, virtualization, cloud storage management", 
    "Answer: A. Text analytics, language understanding, text generation", ""],
    
    ["What are common features of NLP workload scenarios?", 
    "A. Sentiment analysis, key phrase extraction, entity recognition", 
    "B. Image classification, object detection, optical character recognition", 
    "C. Translation, speech recognition, language modeling", 
    "D. Data visualization, clustering, regression", 
    "Answer: A. Sentiment analysis, key phrase extraction, entity recognition", ""],
    
    ["What are features and uses for key phrase extraction?", 
    "A. Identifying important words or phrases in a text document, summarizing content, extracting topic keywords", 
    "B. Recognizing and categorizing objects within images, detecting faces, estimating emotional expressions", 
    "C. Translating languages, generating speech from text, analyzing sentiment from text data", 
    "D. Converting handwritten or printed text into machine-readable text, identifying facial landmarks", 
    "Answer: A. Identifying important words or phrases in a text document, summarizing content, extracting topic keywords", ""],
    
    ["What are features and uses for entity recognition?", 
    "A. Identifying and categorizing objects within images, detecting faces, estimating emotional expressions", 
    "B. Recognizing named entities such as people, organizations, and locations in text, extracting useful information from unstructured data", 
    "C. Translating languages, generating speech from text, analyzing sentiment from text data", 
    "D. Converting handwritten or printed text into machine-readable text, identifying facial landmarks", 
    "Answer: B. Recognizing named entities such as people, organizations, and locations in text, extracting useful information from unstructured data", ""],
    
    ["What are features and uses for sentiment analysis?", 
    "A. Translating languages, generating speech from text, analyzing sentiment from text data", 
    "B. Identifying and categorizing objects within images, detecting faces, estimating emotional expressions", 
    "C. Analyzing the emotional tone of text, determining whether text expresses positive, negative, or neutral sentiment", 
    "D. Converting handwritten or printed text into machine-readable text, identifying facial landmarks", 
    "Answer: C. Analyzing the emotional tone of text, determining whether text expresses positive, negative, or neutral sentiment", ""],
    
    ["What are features and uses for language modeling?", 
    "A. Recognizing and categorizing objects within images, detecting faces, estimating emotional expressions", 
    "B. Generating text based on learned patterns in language data, predicting the next word in a sentence", 
    "C. Translating languages, generating speech from text, analyzing sentiment from text data", 
    "D. Converting handwritten or printed text into machine-readable text, identifying facial landmarks", 
    "Answer: B. Generating text based on learned patterns in language data, predicting the next word in a sentence", ""],
    
    ["What are features and uses for speech recognition and synthesis?", 
    "A. Analyzing sentiment from text data, identifying facial landmarks and estimating emotional expressions", 
    "B. Converting spoken language into text, generating spoken language from text", 
    "C. Recognizing and categorizing objects within images, detecting faces", 
    "D. Translating languages, summarizing content, extracting topic keywords", 
    "Answer: B. Converting spoken language into text, generating spoken language from text", ""],
    
    ["What are features and uses for translation?", 
    "A. Analyzing sentiment from text data, identifying facial landmarks and estimating emotional expressions", 
    "B. Converting text from one language to another, enabling communication between speakers of different languages", 
    "C. Recognizing and categorizing objects within images, detecting faces", 
    "D. Generating text based on learned patterns in language data, predicting the next word in a sentence", 
    "Answer: B. Converting text from one language to another, enabling communication between speakers of different languages", ""],
    
    ["What is a common feature of NLP workloads?", 
    "A. Recognizing and categorizing objects within images", 
    "B. Analyzing sentiment from text data", 
    "C. Translating languages", 
    "D. Generating speech from text", 
    "Answer: B. Analyzing sentiment from text data", ""],
    
    ["What is a primary use for key phrase extraction in NLP?", 
    "A. Translating languages", 
    "B. Summarizing content, identifying important words or phrases in a text document", 
    "C. Analyzing sentiment from text data", 
    "D. Generating speech from text", 
    "Answer: B. Summarizing content, identifying important words or phrases in a text document", ""],
    
      ["What are some features of Natural Language Processing (NLP) workloads on Azure?", 
    "A. Text analytics, language understanding, text generation", 
    "B. Image classification, object detection, optical character recognition", 
    "C. Speech recognition, sentiment analysis, translation", 
    "D. Database administration, virtualization, cloud storage management", 
    "Answer: A. Text analytics, language understanding, text generation", ""],
    
    ["What are common features of NLP workload scenarios?", 
    "A. Sentiment analysis, key phrase extraction, entity recognition", 
    "B. Image classification, object detection, optical character recognition", 
    "C. Translation, speech recognition, language modeling", 
    "D. Data visualization, clustering, regression", 
    "Answer: A. Sentiment analysis, key phrase extraction, entity recognition", ""],
    
    ["What are features and uses for key phrase extraction?", 
    "A. Identifying important words or phrases in a text document, summarizing content, extracting topic keywords", 
    "B. Recognizing and categorizing objects within images, detecting faces, estimating emotional expressions", 
    "C. Translating languages, generating speech from text, analyzing sentiment from text data", 
    "D. Converting handwritten or printed text into machine-readable text, identifying facial landmarks", 
    "Answer: A. Identifying important words or phrases in a text document, summarizing content, extracting topic keywords", ""],
    
    ["What are features and uses for entity recognition?", 
    "A. Identifying and categorizing objects within images, detecting faces, estimating emotional expressions", 
    "B. Recognizing named entities such as people, organizations, and locations in text, extracting useful information from unstructured data", 
    "C. Translating languages, generating speech from text, analyzing sentiment from text data", 
    "D. Converting handwritten or printed text into machine-readable text, identifying facial landmarks", 
    "Answer: B. Recognizing named entities such as people, organizations, and locations in text, extracting useful information from unstructured data", ""],
    
    ["What are features and uses for sentiment analysis?", 
    "A. Translating languages, generating speech from text, analyzing sentiment from text data", 
    "B. Identifying and categorizing objects within images, detecting faces, estimating emotional expressions", 
    "C. Analyzing the emotional tone of text, determining whether text expresses positive, negative, or neutral sentiment", 
    "D. Converting handwritten or printed text into machine-readable text, identifying facial landmarks", 
    "Answer: C. Analyzing the emotional tone of text, determining whether text expresses positive, negative, or neutral sentiment", ""],
    
    ["What are features and uses for language modeling?", 
    "A. Recognizing and categorizing objects within images, detecting faces, estimating emotional expressions", 
    "B. Generating text based on learned patterns in language data, predicting the next word in a sentence", 
    "C. Translating languages, generating speech from text, analyzing sentiment from text data", 
    "D. Converting handwritten or printed text into machine-readable text, identifying facial landmarks", 
    "Answer: B. Generating text based on learned patterns in language data, predicting the next word in a sentence", ""],
    
    ["What are features and uses for speech recognition and synthesis?", 
    "A. Analyzing sentiment from text data, identifying facial landmarks and estimating emotional expressions", 
    "B. Converting spoken language into text, generating spoken language from text", 
    "C. Recognizing and categorizing objects within images, detecting faces", 
    "D. Translating languages, summarizing content, extracting topic keywords", 
    "Answer: B. Converting spoken language into text, generating spoken language from text", ""],
    
    ["What are features and uses for translation?", 
    "A. Analyzing sentiment from text data, identifying facial landmarks and estimating emotional expressions", 
    "B. Converting text from one language to another, enabling communication between speakers of different languages", 
    "C. Recognizing and categorizing objects within images, detecting faces", 
    "D. Generating text based on learned patterns in language data, predicting the next word in a sentence", 
    "Answer: B. Converting text from one language to another, enabling communication between speakers of different languages", ""],
    
    ["What is a common feature of NLP workloads?", 
    "A. Recognizing and categorizing objects within images", 
    "B. Analyzing sentiment from text data", 
    "C. Translating languages", 
    "D. Generating speech from text", 
    "Answer: B. Analyzing sentiment from text data", ""],
    
    ["What is a primary use for key phrase extraction in NLP?", 
    "A. Translating languages", 
    "B. Summarizing content, identifying important words or phrases in a text document", 
    "C. Analyzing sentiment from text data", 
    "D. Generating speech from text", 
    "Answer: B. Summarizing content, identifying important words or phrases in a text document", ""],
     ["What are some features of generative AI solutions?", 
    "A. Creating new content such as images, text, or music, based on learned patterns in existing data", 
    "B. Analyzing sentiment from text data, identifying objects within images", 
    "C. Translating languages, summarizing content, extracting topic keywords", 
    "D. Recognizing speech, generating spoken language from text", 
    "Answer: A. Creating new content such as images, text, or music, based on learned patterns in existing data", ""],
    
    ["What are features of generative AI models?", 
    "A. Learning to imitate human behavior, generating realistic images, text, or other content", 
    "B. Analyzing sentiment from text data, identifying objects within images", 
    "C. Translating languages, summarizing content, extracting topic keywords", 
    "D. Recognizing speech, generating spoken language from text", 
    "Answer: A. Learning to imitate human behavior, generating realistic images, text, or other content", ""],
    
    ["What are common scenarios for generative AI?", 
    "A. Image synthesis, text generation, music composition", 
    "B. Sentiment analysis, object detection, optical character recognition", 
    "C. Translation, speech recognition, language modeling", 
    "D. Data visualization, clustering, regression", 
    "Answer: A. Image synthesis, text generation, music composition", ""],
    
    ["What are responsible AI considerations for generative AI?", 
    "A. Ensuring generated content aligns with ethical guidelines, avoiding bias in training data, transparency in model behavior", 
    "B. Analyzing sentiment from text data, identifying objects within images", 
    "C. Translating languages, summarizing content, extracting topic keywords", 
    "D. Recognizing speech, generating spoken language from text", 
    "Answer: A. Ensuring generated content aligns with ethical guidelines, avoiding bias in training data, transparency in model behavior", ""],
    
    ["What are some features of generative AI solutions?", 
    "A. Learning to imitate human behavior, generating realistic images, text, or other content", 
    "B. Analyzing sentiment from text data, identifying objects within images", 
    "C. Translating languages, summarizing content, extracting topic keywords", 
    "D. Recognizing speech, generating spoken language from text", 
    "Answer: A. Learning to imitate human behavior, generating realistic images, text, or other content", ""],
    
    ["What types of tasks can generative AI models perform?", 
    "A. Image synthesis, text generation, music composition", 
    "B. Sentiment analysis, object detection, optical character recognition", 
    "C. Translation, speech recognition, language modeling", 
    "D. Data visualization, clustering, regression", 
    "Answer: A. Image synthesis, text generation, music composition", ""],
    
    ["What are important considerations when deploying generative AI models?", 
    "A. Ensuring ethical use of generated content, addressing potential biases in training data, providing transparency in model behavior", 
    "B. Analyzing sentiment from text data, identifying objects within images", 
    "C. Translating languages, summarizing content, extracting topic keywords", 
    "D. Recognizing speech, generating spoken language from text", 
    "Answer: A. Ensuring ethical use of generated content, addressing potential biases in training data, providing transparency in model behavior", ""],
    
    ["What are some features of generative AI workloads?", 
    "A. Learning to create new content based on patterns in existing data, generating images, text, or music", 
    "B. Analyzing sentiment from text data, identifying objects within images", 
    "C. Translating languages, summarizing content, extracting topic keywords", 
    "D. Recognizing speech, generating spoken language from text", 
    "Answer: A. Learning to create new content based on patterns in existing data, generating images, text, or music", ""],
    
    ["What are common scenarios where generative AI is applied?", 
    "A. Artistic content generation, content creation in entertainment industry, synthetic data generation", 
    "B. Sentiment analysis, object detection, optical character recognition", 
    "C. Translation, speech recognition, language modeling", 
    "D. Data visualization, clustering, regression", 
    "Answer: A. Artistic content generation, content creation in entertainment industry, synthetic data generation", ""],
    
    ["What are key considerations for ensuring responsible use of generative AI?", 
    "A. Mitigating potential harms from generated content, addressing biases in training data, ensuring transparency and fairness", 
    "B. Analyzing sentiment from text data, identifying objects within images", 
    "C. Translating languages, summarizing content, extracting topic keywords", 
    "D. Recognizing speech, generating spoken language from text", 
    "Answer: A. Mitigating potential harms from generated content, addressing biases in training data, ensuring transparency and fairness", ""],
     ["What are some capabilities of the Azure OpenAI Service?", 
    "A. Natural language generation, code generation, image generation", 
    "B. Sentiment analysis, object detection, optical character recognition", 
    "C. Translation, speech recognition, language modeling", 
    "D. Data visualization, clustering, regression", 
    "Answer: A. Natural language generation, code generation, image generation", ""],
    
    ["What are the natural language generation capabilities of Azure OpenAI Service?", 
    "A. Generating coherent and contextually relevant text based on provided prompts or inputs", 
    "B. Analyzing sentiment from text data, identifying objects within images", 
    "C. Translating languages, summarizing content, extracting topic keywords", 
    "D. Recognizing speech, generating spoken language from text", 
    "Answer: A. Generating coherent and contextually relevant text based on provided prompts or inputs", ""],
    
    ["What are the code generation capabilities of Azure OpenAI Service?", 
    "A. Automatically generating code snippets or completing code based on provided context or requirements", 
    "B. Analyzing sentiment from text data, identifying objects within images", 
    "C. Translating languages, summarizing content, extracting topic keywords", 
    "D. Recognizing speech, generating spoken language from text", 
    "Answer: A. Automatically generating code snippets or completing code based on provided context or requirements", ""],
    
    ["What are the image generation capabilities of Azure OpenAI Service?", 
    "A. Generating realistic images based on provided descriptions or concepts", 
    "B. Analyzing sentiment from text data, identifying objects within images", 
    "C. Translating languages, summarizing content, extracting topic keywords", 
    "D. Recognizing speech, generating spoken language from text", 
    "Answer: A. Generating realistic images based on provided descriptions or concepts", ""],
    
    ["What capabilities does the Azure OpenAI Service offer?", 
    "A. Natural language generation, code generation, image generation", 
    "B. Speech recognition, sentiment analysis, translation", 
    "C. Object detection, optical character recognition, language modeling", 
    "D. Data visualization, clustering, regression", 
    "Answer: A. Natural language generation, code generation, image generation", ""],
    
    ["What can the natural language generation feature of Azure OpenAI Service do?", 
    "A. Generate coherent and contextually relevant text based on provided prompts or inputs", 
    "B. Translate languages, summarize content, extract topic keywords", 
    "C. Analyze sentiment from text data, identify objects within images", 
    "D. Recognize speech, generate spoken language from text", 
    "Answer: A. Generate coherent and contextually relevant text based on provided prompts or inputs", ""],
    
    ["What is a key capability of Azure OpenAI Service for code-related tasks?", 
    "A. Automatically generate code snippets or complete code based on provided context or requirements", 
    "B. Analyze sentiment from text data, identify objects within images", 
    "C. Translate languages, summarize content, extract topic keywords", 
    "D. Recognize speech, generate spoken language from text", 
    "Answer: A. Automatically generate code snippets or complete code based on provided context or requirements", ""],
    
    ["What feature of Azure OpenAI Service allows it to generate realistic images?", 
    "A. Image generation capabilities", 
    "B. Natural language generation capabilities", 
    "C. Code generation capabilities", 
    "D. Speech recognition capabilities", 
    "Answer: A. Image generation capabilities", ""],
    
    ["What are some of the capabilities of Azure OpenAI Service?", 
    "A. Natural language generation, code generation, image generation", 
    "B. Sentiment analysis, object detection, optical character recognition", 
    "C. Translation, speech recognition, language modeling", 
    "D. Data visualization, clustering, regression", 
    "Answer: A. Natural language generation, code generation, image generation", ""],
    
    ["What kind of text can the natural language generation capabilities of Azure OpenAI Service produce?", 
    "A. Coherent and contextually relevant text based on provided prompts or inputs", 
    "B. Code snippets or complete code based on provided context or requirements", 
    "C. Summarized content and extracted topic keywords", 
    "D. Translated languages and sentiment analysis results", 
    "Answer: A. Coherent and contextually relevant text based on provided prompts or inputs", ""],
    
    
]

print(data_list)

from PIL import Image, ImageDraw, ImageFont
import textwrap
from gtts import gTTS
import os

image_width = 1920
image_height = 1080
background_color = (0,127,215)
font_color = (255,255,255)
font_size = 80
line_spacing = 6
margin = 70

for idx, data in enumerate(data_list):
    image = Image.new("RGB", (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("HindVadodara-Light.ttf", font_size)
    y_position = margin

    text_to_speak = ""

    for text in data:
        wrapped_text = textwrap.fill(text, width=50)  # Adjust width as needed
        lines = wrapped_text.split('\n')

        for line in lines:
            draw.text((margin, y_position), line, font=font, fill=font_color)
            y_position += font_size + line_spacing
            text_to_speak += line + "\n"

        y_position += line_spacing  # Add extra spacing between wrapped lines

    image.save(f"Gyan_Dariyo_image_{idx+1}.png")
    image.show()
    import time
    time.sleep(50)
    # Convert text to speech and create an audio file
    tts = gTTS(text=text_to_speak, lang='en')
    audio_file_path = f"Gyan_Dariyo_audio_{idx+1}.mp3"
    tts.save(audio_file_path)

from moviepy.editor import ImageClip, AudioFileClip
from gtts import gTTS
import textwrap
video_list = []
default_fps = 24  # Default frames per second for the video clips

for idx, data in enumerate(data_list):
    text_to_speak = "\n".join(data)
    import time
    time.sleep(50)

    # Convert text to speech and create an audio file
    tts = gTTS(text=text_to_speak, lang='en')
    audio_file_path = f"Gyan_Dariyo_audio_{idx+1}.mp3"
    tts.save(audio_file_path)

    # Load the audio clip
    audio_clip = AudioFileClip(audio_file_path)

    # Get the audio duration
    audio_duration = audio_clip.duration

    # Create an image clip
    image_path = f"Gyan_Dariyo_image_{idx+1}.png"
    image_clip = ImageClip(image_path)

    # Set the audio of the image clip
    video_clip = image_clip.set_audio(audio_clip)

    # Set the duration of the video clip to match the audio duration
    video_clip = video_clip.set_duration(audio_duration)

    # Set the fps for the video clip
    video_clip = video_clip.set_fps(default_fps)

    # Write the final video
    video_file_path = f"Gyan_Dariyo_video_{idx+1}.mp4"
    video_list.append(f"Gyan_Dariyo_video_{idx+1}.mp4")
    video_clip.write_videofile(video_file_path, codec="libx264", audio_codec="aac")

    # Print a message to indicate completion
    print(f"Video {idx+1} created: {video_file_path}")
import time
from gtts import gTTS

def create_combined_mp3(data_list, output_file):
    combined_text = " ".join(data_list)
    import time
    time.sleep(50)
    tts = gTTS(text=combined_text, lang='en')
    tts.save(output_file)
    print(f"Created combined MP3: {output_file}")

for i in range(len(data_list)):
    output_file = f"combined_output_{i+1}.mp3"
    create_combined_mp3([str(data_list[i])], output_file)
from moviepy.editor import VideoFileClip, concatenate_videoclips

video_list = []

for idx, data in enumerate(data_list):
    video_file_path = f"Gyan_Dariyo_video_{idx+1}.mp4"
    video_clip = VideoFileClip(video_file_path)
    video_list.append(video_clip)

final_video = concatenate_videoclips(video_list)

final_video_file_path = "Gyan_Dariyo_final_video.mp4"
final_video.write_videofile(final_video_file_path, codec="libx264", audio_codec="aac")

print(f"Final video created: {final_video_file_path}")

