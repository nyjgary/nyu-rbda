# import libraries 
import re

# hard code search terms 
SEARCH_TERMS = ['hackathon', 'Dec', 'Chicago', 'Java']

# main function to perform word count (non-MapReduce)
def main(input_file='input_data.txt'): 
    
    """ Count number of tweets containing each search term (not case sensitive)
    
    Parameters
    ----------
    input_file: string
        Path to input file containing lines of tweet data, each line of the 
        form: Date,Time;Name,Tweet
            
    Returns
    -------
    tweet_counts: dict
        Dictionary of key-value pairs representing the number of lines (value)
        containing each search term (hardcoded in SEARCH_TERMS). 
        * Also prints out each pair line by line * 
    
    """
    
    # create dict to hold mapping of lowercase term to original term 
    term_mapping = {ori_term.lower(): ori_term for ori_term in SEARCH_TERMS}
    
    # initialize dict to hold counts of each lowercase term 
    counts = dict.fromkeys(term_mapping.keys(), 0)
    
    # read in data line by line, split each line int words  
    with open(input_file) as f:
        for line in f: 
            words = re.split('\W+', line.lower()) 
            # check for appearance of search terms 
            for norm_term in counts:
                if norm_term in words:
                    counts[norm_term] += 1 
    
    # map lowercase term back to original search terms 
    final_counts = {term_mapping[norm_term]: counts[norm_term] for norm_term in counts}
    
    # print results 
    for k, v in final_counts.items():
        print('{}: {}'.format(k, v))
    
    return final_counts

# execute main function 
if __name__ == "__main__":
    main()