birds = ["robin","finch","parakeet","crow"]

puts "What kind of bird is in the cage?"
word = gets.chomp
puts {}

def includer?(array,user_input)
  
   array.each do |x|

      if x == user_input
         return true
      else
         return false
      end 
     
   end

end

puts includer?(birds,word) ? "Tweet-tweet": "Meow"
