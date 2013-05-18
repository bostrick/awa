=========================================================================
Standing on the Shoulders of Giants
=========================================================================

What Open Source has to teach us about the new digital age.

.. contents::

----------------------------------------
Where We've Been
---------------------------------------- 

The Cathedral and the Bazaar
===================================

    http://www.catb.org/esr/writings/homesteading/  (Eric Raymond, 1997)

    + The Cathedral

        - Software is maintained by priests

        - Priests bestow releases upon the people

        - People can gripe about bugs and suggest improvements, but changes 
          must be implemented by priests.

    + The Bazaar

        - Everyone can participate: innovate, fix, modify, share

        - Role of project "maintainer" becomes important

        - Respect for not "forking", but right to revolt

        - Release early and often

        - Treating your users as co-developers is your least-hassle route to
          rapid code improvement and effective debugging.

        - Given a large enough beta-tester and co-developer base, 
          almost every problem will be characterized quickly and 
          the fix obvious to someone.

                "Linus's Law": Given enough eyeballs, all bugs are shallow.

        - If you treat your beta-testers as if they're your most valuable
          resource, they will respond by becoming your most valuable resource.

        - Any tool should be useful in the expected way, but a truly 
          great tool lends itself to uses you never expected.

Open Source Licensing
===================================

    http://opensource.org

    http://www.fsf.org

    + GPL, LGPL, Apache, Artistic, BSD, MIT, ZPL, ...

    + True test: freedom to "distribute" modifications

    + Free as in speach, not as in beer

What has been built
===================================

    + Infrastructure: Linux, FreeBSD, Android, glibc, bash, xorg-X11, GNOME, KDE,...

    + Servers: Apache, BIND, CUPS, sendmail, postfix, ...

    + Databases: MySQL, PostgreSQL, mongodb, ...

    + Applications: (Netscape), Firefox, Chrome, GnuPG, gnuplot, LaTeX, ...

    + Developer: gcc, eclipse, vi, emacs, git, SVN, CVS, ...

    + Interpreters: Python, Ruby, JavaScript, PHP, TCL, Lua, Haskell, Perl, squeak, ...  (OpenJDK!)

    + Frameworks: Drupal, Django, Zope, Pyramid, jQuery, ...

When do I use open source software?
=========================================

    + With every Google search and every Amazon purchase
    
    + In 7 out of 10 smartphones 

        (http://techland.time.com/2013/04/16/ios-vs-android/)

        ======= =========      ========   ==============
        Market  Android        IOS        Other
        ======= =========      ========   ==============
        US      52%            43%        5% 
        Global  70%            21%        9%
        ======= =========      ========   ==============

    + Home Routers, Televisions...
    
    + Gas Pumps (Gilbarco: 50% market share)

A Cathedral of Our Age
================================

    + Many, many people have devoted lifetimes to building Linux and many
      other indispensable Open Source products

Core Internet Protocols
==================================

    + Not Software, so not licensed as Open Source, but lessons 
      to be learned from openness as well

    + RFC: "Request for Comment"

        ======= =========== ======= 
        RFC     Protocol    Year
        ======= =========== ======= 
        114     FTP         1971
        760     IPv4        1980
        768     UDP         1980
        793     TCP         1981
        821     SMTP        1982
        826     ARP         1982
        854     Telnet      1983
        1034    DNS         1987
        1059    NTP         1988
        1094    NFS         1989
        1321    MD5         1992
        1436    Gopher      1993
        1459    IRC         1993
        1487    LDAP        1993
        1631    NAT         1994
        1883    IPv6        1995
        1945    HTTP        1996
        2109    HTTP cookie 1997
        2246    TLS         1999
        2448    iCal        1998
        3783    iSCSI       2004
        4287    Atom        2005
        4251    SSHv2       2006
        4353    SIP         2006
        4646    Lang Codes  2006
        6455    WebSocket   2011
        ======= =========== ======= 

    + No Fees, Simple Text

    + **Low Barrier to Entry**
        

----------------------------------------
What's New
---------------------------------------- 

The Printing Press: Everyone's a Reader
=================================================
    
    +  1450s

    + Undeniably one of the most transformative technologies

    + Luther's 95 Thesis (1517) didn't stay on the door
    
    + New concepts and regulations were needed:  Copyright (1662)


The Internet: Everone's a Publisher
===============================================

    + Just as transformative of a technologly

    + New Concepts and Regulations are needed:  How does instantanious, 
        perfect, global copying effect concepts like Copyright?  

    + Software is the only item that comes under four major Intellectual
      Property frameworks: Copyright, Trademark, Patent, Trade Secret

The Cloud: Pervasive Networking
===============================================

    + Realizaton of Danny Hillis' vision - 2003(?)::

            ... pretty soon you'll have no more idea of what computer you're
            using than you have an idea of where your electricity is generated
            when you turn on the light.

        http://www.wired.com/wired/archive/2.01/kay.hillis_pr.html

    + Global, instananeous publishing available to anyone for $0.12/hour

The Smart Phone: Pervasive Computing
=================================================

    + Android (2008), iPhone (2007)
    
    + Now we're all carrying little computers around in our pockets

    + I can't wait until we figure out how to effectively use them!

    + What an amazingly fun time to be alive...

-------------------------------------------------
Why is this different than 2003?
-------------------------------------------------

We don't need 100,000 copies of databases, we need 1
=============================================================

    + (1 really means 4 or 5 parallel competeing versions)

    + Example: Google Maps

        + We don't need to buy individual streetmaps anymore

        + We use the one copy (possibly cached locally)

        + Again, 4 or 5: Google Maps, MapQuest, Yahoo Maps, Apple Maps(?), 
          OpenStreetMap

    + Census Data

    + Centers for Disease Control and Prevention

We don't need 100,000 copies of multimedia, we need 1
=============================================================

    + (1 really means 4 or 5 parallel competeing versions)
    
    + Examples: 

        + Pandora, Rhapsody, RDIO, ...

        + Netflix, Hulu, YouTube, ...

        + Images ?


We don't need 100,000 copies of software, we need 1
=============================================================

    + (1 really means 4 or 5 parallel competeing versions)

    + Gmail (Yahoo mail, msn mail, apple mail, ...)

    + Not 100,000 copies of Eudora on every system


Solutions can be published instantly
=============================================================

    + GitHub

    + //ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js

    + yum, apt-get

------------------------------------------------------
What problems will be solved in this new world?
------------------------------------------------------

Academic Publishing
=================================

    + Talking about undergraduate and under (the "90% right" regime)

    + It hurts to watch my 12 year old daughter's backpack

    + How it can be done right

        + A Wikipedia style repository of knowledge with 
          established process of moderation

        + Ability to organize selected portions into sylliabus
          for specific audiences

    + How it can be done wrong

        + $80 for electronic access to academic curriculum which expires
          at the end of the year

Church Hymnals
===================================

    + A legacy Nook could be placed in every pew for the amount 
      (I suspect) it cost for a new hymnal

    + Easily customized flow of information for a particular Sunday

    + Coordinated focus of attention

Inverted Market Place
======================================

    + I need a dozen lightbulbs and some toilet paper delivered within 
      the next two weeks

    + I'll review bids in 2 days and select a vendor

Karma - the Post Legal Era
=========================================

    + What industry to obsolete next?  Legislatures...

    + The price of a candy bar is decided by capturing and quantifying
      our individual weighting of relative wants.

    + Can we capture and quantify our individual assessments of relative
      good and bad in everyday situations?

    + Extend the reach of the invisible hand....

Example: Electronic Prescriptions
=========================================

    + Doctor types it in on his laptop

    + It gets zoomed over to local pharmacy

    + I get there and it's wrong....

    + The person most vested in a correct outcome (me)
      has zero visibility into the process

    + Why should I trust them any more than I trust video poker machines?

    + Notably Lax Security

        + Physical Insecurities

        + Admitted Dropped Votes

        + Common Locks

        + Common Admin Passwords    


    + Whose audit trail am I relying on?

        https://www.schneier.com/blog/archives/2006/05/diebold_doesnt.html

        This quote sums up nicely why Diebold should not be trusted to secure election machines:

    David Bear, a spokesman for Diebold Election Systems, said the potential risk existed because the company's technicians had intentionally built the machines in such a way that election officials would be able to update their systems in years ahead.

    "For there to be a problem here, you're basically assuming a premise where you have some evil and nefarious election officials who would sneak in and introduce a piece of software," he said. "I don't believe these evil elections people exist."

If you can't get the threat model right, you can't hope to secure the system.

    + http://media3.washingtonpost.com/wp-dyn/content/graphic/2006/03/16/GR2006031600213.gif


Example: Richmond County Tax Maps
====================================

    + Proprietary Software Required

    + My money pays for the data and the service... Why isn't it
      available with low bariers?

------------------------------------------------------
How to do it
------------------------------------------------------

Google Maps
============================================

    + APIs are publically available



Google Dashboard
===========================================

    + The person most vested in the data has access to it and
      control of it


------------------------------------------------------
How do we app
------------------------------------------------------

What Lessons can we Learn from Open Source?
===================================================


    + Low barriers to entry   ("View Source...")

    + Empower people with knowledge

    + Encourage Innovation

Final Thoughts
=================================================


    + How Much Can Children Teach Themselves?

        + http://www.npr.org/2013/04/25/179010396/unstoppable-learning

        + Sugata Mitra, Professor of Education, Newcastle University, NIIT

        + "Hole in the Wall" experiments 1999

            + Set kiosk up with computer in New Delhi Slum, remote Indian
              Village

                + Children who know no English, no Internet, and given
                  on instructions.

                + Can we touch it?   Sure...

                + We had to teach ourselves English first...

                + Paint opens, Word opens, kids figured out character map
                  application for key-board

            + It's not about making learning happen... 
                 It's about letting it happen.  

        + It's not about making innovation happen... 
                 It's about making

                + What would have happended if these kids could have
                  said "View Source?"   They would learn how to solve
                  their problems which we can't envision.

    + Let's build higher cathedrals by stading on the shoulders of giants...

