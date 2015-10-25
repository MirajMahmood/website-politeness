/**
 * Created by Ali on 10/25/15.
 */

// Generic imports
import java.util.*;

// Py4J imports
import edu.stanford.nlp.ling.tokensregex.CoreMapSequenceMatchAction;
import py4j.GatewayServer;

// Stanford CoreNLP imports
import edu.stanford.nlp.ling.*;
import edu.stanford.nlp.pipeline.*;
import edu.stanford.nlp.sentiment.CollapseUnaryTransformer;
import edu.stanford.nlp.trees.*;
import edu.stanford.nlp.util.*;

public class TreeMaker {
    // Data members
    private Properties properties;
    private StanfordCoreNLP pipeline;
    private Annotation annotation;
    private CollapseUnaryTransformer collapser;
    private TreePrint tp;

    public Treepack parse(String text){
        // To return
        Treepack ret = new Treepack();

        // Clean text and annotate
        text = text.replaceAll("(^\")|(\"$)", "");
        annotation = new Annotation(text);
        pipeline.annotate(this.annotation);

        // Fetch the trees
        List<CoreMap> sentences;
        sentences = annotation.get(CoreAnnotations.SentencesAnnotation.class);
        if(sentences.size() == 1){
            ret.count = 1;
            ret.first = sentences.get(0).get(TreeCoreAnnotations.BinarizedTreeAnnotation.class).toString();
        }
        else if(sentences.size() == 2){
            ret.count = 2;
            ret.first = sentences.get(0).get(TreeCoreAnnotations.BinarizedTreeAnnotation.class).toString();
            ret.second = sentences.get(1).get(TreeCoreAnnotations.BinarizedTreeAnnotation.class).toString();
        }

        return ret;
    }

    private TreeMaker(){
        // Initialize all the tools needed for annotation
        // The annotation pipeline
        System.out.println("TreeMaker being born...");
        properties = new Properties();
        properties.put("annotators", "tokenize, ssplit, parse, sentiment");
        pipeline = new StanfordCoreNLP(properties);

        // For collapsing dummy terminals at tree end
        collapser = new CollapseUnaryTransformer();

        // For formatting the tree output
        tp = new TreePrint("oneline");
    }

    public static void pain(String args[]){
        TreeMaker tm = new TreeMaker();
        tm.parse("Hello people of the world!");
    }

    public static void main(String args[]){
        TreeMaker tm = new TreeMaker();
        GatewayServer server = new GatewayServer(tm);
        System.out.println("Serving Python requests...");
        server.start();
    }
}
