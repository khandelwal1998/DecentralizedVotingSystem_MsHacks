pragma solidity ^0.4.18;

contract Coursetro {
    struct candidate{
    
   string fName;
   int age;
    }
    struct votes
    {
        bytes32 candname;
    }
    uint c;
    uint c1;
    mapping (uint => candidate) public allFiles;
    mapping (uint => votes) public allvotes;

  function setCandidate(string _fName, int _age) public {
      c=c+1;
      allFiles[c]=candidate({fName:_fName,age:_age});
  }
   
   function Vote(bytes32 name)public  {
       c1=c1+1;
      allvotes[c1]=votes({candname:name});   }
      
   function TotalVotes() public returns (uint) 
   {
       return(c1);
   }
   function getAll() public returns(bytes32[10])
   {
       bytes32[10] bytesstr;
       for(uint256 i=1;i<=c1;i++)
       {
           votes memory p=allvotes[i];
           bytesstr[i]=p.candname;
         
       }
       return(bytesstr);
   }
   
}