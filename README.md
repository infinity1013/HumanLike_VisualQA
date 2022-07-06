# Human Like Visual Question Answering System

## Aim 
Smart Doc VQA system is Deep learning Web application implemented using Keras and TensorFlow on Flask framework. The Web app is meant to answer the question asked by user related to document uploaded by the same user.
Given a document and question asked related to document this model is able to generate answer by forming context from document.

## Theory 
The main task of the algorithm can be divided into two sections: 
Firstly, it should accurately get the features from the document and question asked from the user. 
The second part of the algorithm is to get answer from features 

### Document Processing
The document could not be given directly as machine does not understands it. We need to process first and then give to our model.
The features of the document are extracted by dividing the document into 9 ROI’s.</br>
• **Heading/Title** The title or caption of a page, chapter, etc. </br>
• **Subtitle/Byline** The secondary or subordinate title of a page or a line of text giving the author’s name. </br>
• **Paragraph/Body** The main text that would be read. </br>
• **Picture** The picture or image that contains no text or data. </br>
• **Caption** The text placed next an image, data, etc. that provides or explains information about an image or data.</br>
• **List** Typically bulleted lists, where each bullet is not a full sentence. </br>
• **Data** Tables, charts, graphs, infographic, or other figures with data or information. </br>
• **Sub-data** The text placed inside of the Data region. </br>
• **Other** Any other text that does not fit in the other categories. </br>

For this we need image processing algorithm **FasterRCNN**. We applied fasterRCNN using **Detectron2** Facebook library. One can apply on your own dataset and get your model trained with its different variants.</br>
<img src="https://user-images.githubusercontent.com/68748614/173341559-b866913b-9a8e-4574-93cd-2eee77af4408.png" width="500" height="550" />
<img src="https://user-images.githubusercontent.com/68748614/173341619-2d42b2f1-4077-4d83-a286-ca63ea24c057.png" width="500" height="550" />

Link to detectron -> https://github.com/facebookresearch/detectron2 </br>
Colab notebook -> https://colab.research.google.com/drive/16jcaJoc6bCFAQ96jDe2HwtXj7BMD_-m5
 
After segmenting document into ROIs except for image we need to get text from it which we did by using **py-tesseract**. When we got text we clubbed into one as context vector which we nee to pass to our question answering module. </br>
Pytesseract -> https://pypi.org/project/pytesseract/


### Question Answering 
Answer Generation Module is the main core of project which is trained on 10,000 images collected from different blogs, news article on internet. The input to the model will be features collected from first module.

There are many question answering models available but we used T5 i.e. We trained through our dataset but you can use pre-trained also if you don’t need your question answering model to get train to question of specific domain field.

For T5 training refer to youtube channel->https://www.youtube.com/watch?v=r6XY80Z9eSA </br>
Their github->https://github.com/curiousily/Getting-Things-Done-with-Pytorch</br>
<img src="https://user-images.githubusercontent.com/68748614/173341047-9bb98f98-8457-4780-81a6-45d3a4effdb6.png" width="400" height="450" />
<img src="https://user-images.githubusercontent.com/68748614/173341305-b5a2e578-185c-448f-b1d5-5d74515522d5.png" width="550" height="450" />


## APPLICATION 
1) Creating intelligent agents that can answer questions as well as people is a long-cherished goal of artificial intelligence. To achieve this goal, machine reading comprehension is a great challenge to enable a machine to read and understand natural language texts so that it can answer questions, asked by user related to the context. </br>
2) In studies it has been discovered that mostly question asked by visually impaired users involves images in the surrounding which involves reading text from image. But today’s visual question answering system cannot read on its own. </br>
3) The MRC capability can be valuable to users when employed by automated assistants like customer-service chat bots on e-commerce website or assistant systems for reading professional literature. </br>
4) In this many real-world documents are provided in non-plain text formats. When we search on internet, we get relevant documents in order and ranked by user deduced keywords based on various aspects such as popularity measures, keyword matching, frequencies of accessing documents, etc. Howsoever, they don’t really the fulfil the task of information retrieval as documents still have to be examined one by one to obtain the required information, it makes information retrieval a time consuming process. So this Q&A system along with document retrieval could solve this problem to give accurate and exact result in less time.

## Further improvements
This is basic question answering from document but to get more accurate and robust answers you can create more variants by putting positional embedding, etc refer to latest paper of 2021

## Web Application Preview
<p align="center">
 <img src="https://user-images.githubusercontent.com/68748614/173341383-d9cb7dc2-7d66-410d-bef4-eae45e84c21f.png" width="800" height="400" />
</p>

</br>
<p align="center">
 <img src="https://user-images.githubusercontent.com/68748614/173341416-23da5e29-cc2d-4587-89cc-73935b0c1795.png" width="800" height="400" />
<p>

### Reference Video
https://drive.google.com/file/d/1rTV_O4HFIFnwIY-wRkIjPNF_FC5w6VOH/view?usp=sharing


