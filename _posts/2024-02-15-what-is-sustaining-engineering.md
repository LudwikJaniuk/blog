---
title: "What is Sustaining Engineering? (draft)"
date: 2024-02-15
---

![Sherlock Holmes Duke representing Sustaining](/assets/images/sherlock-duke.png)

I studied computer science because I thought I wanted to write code for a living, but deep down, maybe I just wanted to know how things work under the hood. This is entitled - I cannot accept that I should not be permitted to look behind the magician's curtain. If not for this I would not have tortured myself learning C++.

This summer will mark my third year in the Java Platform Group at Oracle. When hiring me for the _JVM Sustaining Engineering_ team, they told me I wouldn't be writing code, but keeping code running. "Won't I be bored?" I asked. 

Here's what I've learned so far. The whole world depends on the JVM - we're running "more than 60 billion Java Virtual Machines worldwide"[^1] and in places I never expected[^2]. Some years ago, the OpenJDK adopted a time-based release model acknowledging that there are "developers, who prefer rapid innovation, and enterprises, which prefer stability"[^3]. But that stability is not the same as doing nothing[^4]. Cryptographic algorithms change under our feet, as do operating systems, and even compilers. Vulnerabilities and bugs are discovered regularly. **Sustaining Engineering** means reacting to those changes[^5] to deliver this stability that Java is so valued for. 

If the JVM doesn't perform as expected, there is a lot of real-world pain. A car factory grinds to a halt. A hospital cannot schedule operating rooms. A bank is out of service, and people don't get paid on time[^6]. These things happen extremely rarely, but when they do, we're the ones to act on them. Sustaining Engineering means solving the underlying issue, while also helping the customer work around the problem.

I haven't had a boring day yet.

[^1]: [https://www.oracle.com/java/](https://www.oracle.com/java/)
[^2]: Like SIM cards! [https://www.oracle.com/java/java-card/](https://www.oracle.com/java/java-card/)
[^3]: [https://mreinhold.org/blog/forward-faster](https://mreinhold.org/blog/forward-faster)
[^4]: [https://en.wikipedia.org/wiki/Red_Queen%27s_race](https://en.wikipedia.org/wiki/Red_Queen%27s_race) and [https://www.ascm.org/ascm-insights/the-red-queen-hypothesis/](https://www.ascm.org/ascm-insights/the-red-queen-hypothesis/)
[^5]: [https://www.oracle.com/security-alerts/](https://www.oracle.com/security-alerts/)
[^6]: Even worse, should the JVM emit incorrect machine instructions, an incorrect balance could be stored after a transaction - imagine losing millions that way. A permeating principle in the codebase is to always prefer crashing rather than even risk incorrect execution. 
