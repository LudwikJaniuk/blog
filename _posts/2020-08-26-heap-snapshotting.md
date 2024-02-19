---
title: "Direct Heap Snapshotting in the Java HotSpot VM: a Prototype"
date: 2020-08-26
---

_This is a repost of my blog entry about my master thesis at Oracle. The original was [published on inside.java](https://inside.java/2020/08/26/heap-snapshotting/)_

Hi! I’m Ludvig, a CS student from Stockholm. I am currently finishing my 5-year education with a focus on Theoretical Computer Science and moving on towards professional work. My background includes volunteer work organizing hackathons and the yearly djulkalendern CTF challenge, an exchange in Barcelona, startup work, R&D with Augmented Reality, and Teaching Assistant positions in various courses at KTH including on algorithms and interaction programming. My goals for the summer include learning Rust and Clojure at a deeper level.

In my master thesis at Oracle, I have investigated “Heap Snapshotting”, which is an approach that could potentially reduce JVM startup time. In broad strokes, given that JVM initialization takes a lot of time, but is assumed to be quite deterministic, can’t we just take a snapshot of the whole heap at the end of initialization, and use it at the next startup to start directly from that initialized state? We might have to do some “fixup procedures” to make sure that the snapshot can actually start, but assuming those don’t take too much time, it should save us startup time.

![heap snapshotting timeline diagram](/blog/assets/images/heap-snapshotting.png)

So can this be done? Or is the JVM too complex to support such a coarse operation? And how are the time results in practice?

It turns out that yes, it can be done since I have been able to achieve such a restoration. The snapshot is taken very early, in the function Threads::initialize_java_lang_classes, and Epsilon GC is used to simplify not having to deal with any garbage collection, and to get a contiguous heap. There are many more such simplifications, fixing those is left for future work.

The question is whether such a snapshot is stable. Can we trust that the restored state will work? We have good reasons to be suspicious, but my implementation passes all relevant tests included in the OpenJDK distribution, as well as testing on several applications running on it.

Another positive, and unexpected result is that already in this small prototype, there is some minuscule time gain. That is to say, the time saved by the snapshot is larger than the time it takes to load the snapshot and fix it up. I would have been satisfied with my work even if this had not been the case, but it is nice to see.

The big results however are expected to be seen when someone continues my work in the future. The Heap Snapshot Point (see the illustration) can and should be pushed later in the timeline. Each next step covered by the snapshot means more time saved on initialization. The long-term vision is to not only snapshot the JVM initialization, but also the deterministic parts of actual programs written in Java, through an API exposed to the programmer. Maybe there could even be a whole type-system marking nondeterministic parts of the state and other sensitive things for automatic removal?

While it does feel bad to have to stop right when I have gotten good at debugging errors in the JVM and pushing that snapshot point further and further, my master thesis period is at an end. I do believe it will fall in competent hands in the future, as Oracle is already planning to bring in more master students. In the end, I have learned an incredible amount during my time at Oracle, with the people at the JPG office in Stockholm, and could not have imagined a better master thesis period.

As to why I chose Oracle for my thesis, I’ll admit I was skeptical at first since it is a very large company. However, I happened to sit down with a few engineers from Oracle at a career fair dinner, and I was a bit charmed by the laid-back competence they displayed. I did get the impression that these were real experts, and I could definitely learn a lot from them. It turned out in the end that Oracle’s offer fit my skills the best, so motivated by the personal experience, I took them up on the offer, and have not been disappointed.

I’d like to end by thanking everyone at the JPG office in Stockholm for their patience, willingness to share knowledge, and for making me feel like part of the team. I direct special thanks to Ioi Lam and Tobias Wrigstad for devoted time. My thesis results would not have been possible without them.
