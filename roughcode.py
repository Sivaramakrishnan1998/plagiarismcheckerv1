# dataextract code

    
                        <div class="col-sm-5">
                            
                            <div class="form-box">
                                <div class="form-top">
                                    <div class="form-top-left">
                                        <h3>Sign up now</h3>
                                        <p>Fill in the form below to get instant access:</p>
                                    </div>
                                    <div class="form-top-right">
                                        <i class="fa fa-pencil"></i>
                                    </div>
                                </div>
                                <div class="form-bottom">
                                    <form role="form" action="" method="post" class="registration-form">
                                         {% csrf_token %}
                                         {{ form.non_field_errors }}
                                        <div class="form-group">
                                            <label class="sr-only" for="username">Username</label>
                                            <input type="text" name="username" placeholder="Username" class="form-first-name form-control" id="form-first-name">
                                        </div>
                                        
                                        <div class="form-group">
                                             <label class="sr-only" for="email">Email</label>
                                            <input type="text" name="email" placeholder="Email..." class="form-email form-control" id="form-email">
                                        </div>
                                        <div class="form-group">
                                             <label class="sr-only" for="institute">Institute Name</label>
                                            <input type="text" name="institute" placeholder="Institute Name..." class="form-email form-control" id="form-institute">
                                        </div>
                                        <div class="form-group">
                                             <label class="sr-only" for="address">Address</label>
                                            <input type="text" name="address" placeholder="Address..." class="form-email form-control" id="form-address">
                                        </div>
                                        <div class="form-group">
                                              <label class="sr-only" for="password1">Password</label>
                                            <input type="password" name="password1" placeholder="Password..." class="form-password form-control" id="form-password">
                                        </div>
                                        <div class="form-group">
                                            <label class="sr-only" for="password2">Password</label>
                                            <input type="password" name="password2" placeholder="Re-type Password..." class="form-password form-control" id="form-password">
                                        </div>
                                        <button type="submit" name = "insregisterbutton"class="btn">Sign me up!</button>  
                                    </form>
                                </div>
                            </div>
                            
                        </div>

def dataextract(urllist,textss):
    f = io.open('file1.txt','w', encoding="utf-8")
    f.truncate()
    f.close()
    toplist = urllist[:1]
    for l in toplist:

        print(l)
        if (l!='/' and len(l)>2):
            html = get('http://%s'%(l),verify = False,headers = headers).text
            soup = BeautifulSoup(html)
            # kill all script and style elements
            for script in soup(["script", "style"]):
                script.extract()
                # get text
            text = soup.get_text()
            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in text.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # drop blank lines
            text = '\n'.join(chunk for chunk in chunks if chunk)
            z = io.open('file1.txt','a', encoding="utf-8")
            z.write(text)
            z.close()
            print(text)
    d1 = io.open('file1.txt','r', encoding="utf-8")

    file1_data = d1.read()
    file2_data = textss
    similarity_ratio = calplag(file1_data,file2_data)
    #similarity_ratio = SequenceMatcher(None,file1_data,file2_data).ratio()
    d1.close()

    return similarity_ratio

# def show function 

def show(request,string):
    sent=[]
    textsent = []
    matchsent = []
    fulllist = []
    parsed = urlparse(string)
    root, ext = splitext(parsed.path)
    if ext=='.pdf':
        html = get('http://%s'%(string),verify = False,headers = headers,stream=True)
        with open("syed.pdf","wb") as pdf:
            for chunk in html.iter_content(chunk_size=1024):

                 # writing one chunk at a time to pdf file
                 if chunk:
                     pdf.write(chunk)
            pdf.close()
            docdata = open('syed.pdf','rb')
            pdfReader = PyPDF2.PdfFileReader(docdata)

            num_pages = pdfReader.numPages
            count = 0
            text = ""

            while count < num_pages:
                pageObj = pdfReader.getPage(count)
                count +=1
                text += pageObj.extractText()
    else:
        html = get('http://%s'%(string),verify = False,headers = headers).text
        soup = BeautifulSoup(html)
        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()
            # get text
        text = soup.get_text()
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
    text =  re.sub('[!@#$\n\t0123456789]','',text)
    text=text.replace("'","")
    text = text.replace("(","")
    text = text.replace(")","")
    text = text.replace("-","")
    text = text.replace("_","")
    text = text.replace('"','')
    text = text.replace('[','')
    text = text.replace(']','')
    text = text.replace('^','')
    text = text.replace('?','')
    text = text.replace('*','')
    text = text.replace('=','')
    text = text.replace('+','')
    text = text.replace('%','')
    text = text.replace(';','')
    url = 'http://%s'%string
    m = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', text)
    for senten in m:
        textsent.append(senten)
    d1 = io.open('sentences.txt','r', encoding="utf-8")
    file1_data = d1.read()
    file1_data =  re.sub('[!@#$\n\t0123456789-]','',file1_data)
    file1_data=file1_data.replace("'","")
    file1_data=file1_data.replace("(","")
    file1_data=file1_data.replace(")","")
    file1_data=file1_data.replace("-","")
    file1_data=file1_data.replace("_","")
    file1_data=file1_data.replace('"','')
    file1_data=file1_data.replace('[','')
    file1_data=file1_data.replace(']','')
    file1_data=file1_data.replace('^','')
    file1_data=file1_data.replace('?','')
    file1_data=file1_data.replace('*','')
    file1_data=file1_data.replace('=','')
    file1_data=file1_data.replace('+','')
    file1_data=file1_data.replace('%','')
    file1_data=file1_data.replace(';','')

    m = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', file1_data)
    for senten in m:
        sent.append(senten)
    d1.close()
    print(len(sent))
    for se in sent:
        # print(se)
        gg = difflib.get_close_matches(se[:180],textsent,n=4,cutoff=0.3)
        matchsent.append(gg)

    for se in matchsent:
        for s in se:
            fulllist.append(s)
    print(fulllist)
    print(len(fullist))
    json_list = json.dumps(fulllist)
    return render(request,'show.html',{'text':text,'url':url,'sentences':json_list,'l':len(matchsent),})




# pdf rendering

class Render:

    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)





# importing files through the requests module
files = {"file": ('b839', open('/home/user/b839.jpeg', 'rb'), 'multipart/form-data')}
resp = requests.post('http://localhost:8000/api/upload/', files=files)


<script language=JavaScript>
/*
 * This is the function that actually highlights a text string by
 * adding HTML tags before and after all occurrences of the search
 * term. You can pass your own tags if you'd like, or if the
 * highlightStartTag or highlightEndTag parameters are omitted or
 * are empty strings then the default <font> tags will be used.
 */
function doHighlight(bodyText, searchTerm, highlightStartTag, highlightEndTag)
{
  // the highlightStartTag and highlightEndTag parameters are optional
  if ((!highlightStartTag) || (!highlightEndTag)) {
    highlightStartTag = "<font style='color:blue; background-color:yellow;'>";
    highlightEndTag = "</font>";
  }

  // find all occurences of the search term in the given text,
  // and add some "highlight" tags to them (we're not using a
  // regular expression search, because we want to filter out
  // matches that occur within HTML tags and script blocks, so
  // we have to do a little extra validation)
  var newText = "";
  var i = -1;
  var lcSearchTerm = searchTerm.toLowerCase();
  var lcBodyText = bodyText.toLowerCase();

  while (bodyText.length > 0) {
    i = lcBodyText.indexOf(lcSearchTerm, i+1);
    if (i < 0) {
      newText += bodyText;
      bodyText = "";
    } else {
      // skip anything inside an HTML tag
      if (bodyText.lastIndexOf(">", i) >= bodyText.lastIndexOf("<", i)) {
        // skip anything inside a <script> block
        if (lcBodyText.lastIndexOf("/script>", i) >= lcBodyText.lastIndexOf("<script", i)) {
          newText += bodyText.substring(0, i) + highlightStartTag + bodyText.substr(i, searchTerm.length) + highlightEndTag;
          bodyText = bodyText.substr(i + searchTerm.length);
          lcBodyText = bodyText.toLowerCase();
          i = -1;
        }
      }
    }
  }

  return newText;
}


/*
 * This is sort of a wrapper function to the doHighlight function.
 * It takes the searchText that you pass, optionally splits it into
 * separate words, and transforms the text on the current web page.
 * Only the "searchText" parameter is required; all other parameters
 * are optional and can be omitted.
 */
function highlightSearchTerms(searchText, treatAsPhrase, warnOnFailure, highlightStartTag, highlightEndTag)
{
  // if the treatAsPhrase parameter is true, then we should search for
  // the entire phrase that was entered; otherwise, we will split the
  // search string so that each word is searched for and highlighted
  // individually
  if (treatAsPhrase) {
    searchArray = [searchText];
  } else {
    searchArray = searchText.split(" ");
  }

  if (!document.body || typeof(document.body.innerHTML) == "undefined") {
    if (warnOnFailure) {
      alert("Sorry, for some reason the text of this page is unavailable. Searching will not work.");
    }
    return false;
  }

  var bodyText = document.body.innerHTML;
  for (var i = 0; i < searchArray.length; i++) {
    bodyText = doHighlight(bodyText, searchArray[i], highlightStartTag, highlightEndTag);
  }

  document.body.innerHTML = bodyText;
  return true;
}

function searchPrompt(defaultText, treatAsPhrase, textColor, bgColor)
{
  // This function prompts the user for any words that should
  // be highlighted on this web page
  if (!defaultText) {
    defaultText = "";
  }

  // we can optionally use our own highlight tag values
  if ((!textColor) || (!bgColor)) {
    highlightStartTag = "";
    highlightEndTag = "";
  } else {
    highlightStartTag = "<font style='color:" + textColor + "; background-color:" + bgColor + ";'>";
    highlightEndTag = "</font>";
  }

  if (treatAsPhrase) {
    promptText = "Please enter the phrase you'd like to search for:";
  } else {
    promptText = "Please enter the words you'd like to search for, separated by spaces:";
  }

  searchText = defaultText;

  if (!searchText)  {
    alert("No search terms were entered. Exiting function.");
    return false;
  }

  return highlightSearchTerms(searchText, treatAsPhrase, true, highlightStartTag, highlightEndTag);
}

function ondf(){
var days = {{sentences|safe}};
// var days = ["The analysis","This unique information permits the study of the effect of teenspecific price on cigarette demand","You created a paper for presentation in your educational "]
for (var i = 0; i < days.length; i++) {
    searchPrompt(days[i], true, 'green', 'yellow');
}
// {% for sentence in sentences %}
//
// searchPrompt({{sentence}},true,'green','yellow');
//
// {% endfor %}

}
</script>




# For pdf opening code
class Render:

    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)
