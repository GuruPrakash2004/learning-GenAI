chunks = ["chunk1", "chunk2", "chunk3", "chunk4","chunk5"];

print(len(chunks));
print(chunks[2]);
print(chunks[len(chunks)-1]);

chunks.insert(2,"Gopal");
print(chunks);

chunks.append("chunk6");
print(chunks);


chunks.remove("Gopal");
print(chunks);

if "chunk1" in chunks:
    print("the values is in chunks!");
else:
       print("the values is not in chunks!");