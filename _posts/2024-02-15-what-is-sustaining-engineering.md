---
title: "What is Sustaining Engineering? (draft)"
date: 2024-02-15
---


I studied computer science because I thought I wanted to write code for a living, but deep down, maybe I just wanted to know how things work under the hood. This is entitled - I cannot accept that I should not be permitted to look behind the magician's curtain. If not for this I would not have tortured myself learning C++.

This summer will mark my third year in the Java Platform Group at Oracle. When hiring me for the _JVM Sustaining Engineering_ team, they told me I wouldn't be writing code, but keeping code running. "Won't I be bored?" I asked. 

Here's what I've learned so far. The whole world relies on the JVM - we're running "more than 60 billion Java Virtual Machines worldwide"[^1] and in places I never expected[^2]. 
If the JVM doesn't do what it should, there is a lot of real-world pain. A car factory grinds to a halt, a hospital cannot schedule operating rooms. A bank is out of service, and people don't get paid on time[^3]. These things happen extremely rarely, but we're the ones to act on them when they do. In **Sustaining Engineering**, we track down the underlying issue while also helping the customer work around the problem. It's a bit like being a detective.

![Sherlock Holmes Duke representing Sustaining](/assets/images/sherlock-duke-min.png){:style="display:block; margin-left:auto; margin-right:auto"}

Some years ago OpenJDK switched to a time-based "tip and tail" release model acknowledging that there are "developers, who prefer rapid innovation, and enterprises, which prefer stability"[^4][^5].
The tip is the latest Feature Release, coming every six months, and the tail are the LTS releases. My job is caring about the latter. Delivering the stability of the tail, it turns out, is not the same as doing nothing[^6].
Cryptographic algorithms change under our feet, as do operating systems, and even compilers. Vulnerabilities and bugs are discovered regularly. So Sustaining Engineering also means reacting to those changes[^7] to deliver the stability Java is valued for. Ideally we fix issues before they have a chance to harm anyone, and we don’t have to play detectives.

Between wearing those two hats, and much more - I haven't had a boring day yet.


[^1]: [https://www.oracle.com/java/](https://www.oracle.com/java/)
[^2]: Like SIM cards! [https://www.oracle.com/java/java-card/](https://www.oracle.com/java/java-card/)
[^3]: Even worse, should the JVM emit incorrect machine instructions, an incorrect balance could be stored after a transaction - imagine losing millions that way. A permeating principle in the codebase is to always prefer crashing rather than even risk incorrect execution. 
[^4]: [https://mreinhold.org/blog/forward-faster](https://mreinhold.org/blog/forward-faster)
[^5]: [Java 21 By Brian Goetz](https://youtu.be/eXCx2hW_xNI?feature=shared&t=166), Devoxx Belgium 2023
[^6]: [https://en.wikipedia.org/wiki/Red_Queen%27s_race](https://en.wikipedia.org/wiki/Red_Queen%27s_race) and [https://www.ascm.org/ascm-insights/the-red-queen-hypothesis/](https://www.ascm.org/ascm-insights/the-red-queen-hypothesis/)
[^7]: [https://www.oracle.com/security-alerts/](https://www.oracle.com/security-alerts/)

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fblog.janiuk.se&count_bg=%23963DC8&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=true)](https://hits.seeyoufarm.com)
