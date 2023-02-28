# Experimenting with embeddings locally.

I wanted to see how well a small sentence embeddings models can perform. I went to hugging face and checked out some rankings. [This one](https://huggingface.co/sentence-transformers/multi-qa-mpnet-base-dot-v1) scored well, and it's only 420Mb. So I ran [some random pg essay](http://www.paulgraham.com/badeconomy.html) through it. 

To reproduce it, just 
```
pip install -r requirements.txt
python test.py
```

The results are great:

> query:how's the economic situation?
> The economic situation is apparently so grim that some experts fear we may be in for a stretch as bad as the mid seventies. 0.3285517
> query:what should an entrepreneur do right now?
> So maybe a recession is a good time to start a startup. 0.35844052
> query:what should an angel investor do?
> If we've learned one thing from funding so many startups, it's that they succeed or fail based on the qualities of the founders. 0.3809564
> query:I'm a salesperson. What should I do?
> That could be a problem if you work in sales or marketing. 0.42319715
> query:Is a crash coming?
> The economic situation is apparently so grim that some experts fear we may be in for a stretch as bad as the mid seventies. 0.4601699
> query:is this funny?
> In fact, what makes the preceding paragraph true is that most readers won't believe it—at least to the extent of acting on it. 0.5594812
> query:tell me a joke
> Look in the mirror. 0.52308095
> query:what does warren buffett think?
> And like any investor you should buy when times are bad. 0.47173095
