/*
    This is my first YARA rule
    It searches for the following phrase:
    "the correct syntax"
*/

rule Syntax_Police
{
    meta:
        creator = "David Armstrong"
        date = "11/16/2020"
        purpose = "Example of a YARA rule"

    strings:
        //search for the following string
        $string1 = "the correct syntax"
    condition:
        //return the name of the rule if found
        $string1
}
