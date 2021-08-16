 function Anagram(str1,str2)
    {
        // Get lenghts of both strings
        let n1 = str1.length;
        let n2 = str2.length;
   
        // If length of both strings is not same,
        // then they cannot be anagram
        if (n1 != n2)
            return false;
   
        // Sort both strings
        str1.sort();
        str2.sort()
   
        // Compare sorted strings
        for (let i = 0; i < n1; i++)
            if (str1[i] != str2[i])
                return false;
   
        return true;
    }
     
    /* Driver Code*/
    let str1=['t', 'e', 's', 't' ];
    let str2=['t', 't', 'e', 'w' ];
     
    // Function Call
        if (Anagram(str1, str2))
            document.write("The two strings are"
                               + " anagram of each other<br>");
        else
            document.write("The two strings are not"
                               + " anagram of each other<br>");
