<h1>Python /va/log/auth.log analysis</h1>

<h2>Description</h2>
Python script designed to analyze log files, with a focus on /var/log/auth.log. It identifies key information such as command usage, user authentication changes, and security alerts, providing a detailed analysis that enhances the understanding of system behavior and security posture.
<br />


<h2>Languages Used</h2>

- <b>Python</b>

<h2>Environments Used </h2>

- <b>Linux</b>

<h2>Program Overview:</h2>

<p align="center">
Print details of deleted users: <br/>
<img src="https://i.imgur.com/3Tpp1De.png" height="80%" width="80%" alt="Print deleted users"/>
<br />
<br />Print details of newly added users: <br/>
<img src="https://i.imgur.com/TzZagG4.png" height="80%" width="80%" alt="Print user details"/>
<br />
<br />
Print details of commands used:  <br/>
<img src="https://i.imgur.com/kxQMNpl.png" height="80%" width="80%" alt="Print command details"/>
<br />
<br />
Print details of changed password:  <br/>
<img src="https://i.imgur.com/OITjXSF.png" height="80%" width="80%" alt="Print details of changed password"/>
<br />
<br />
Print details of when users used su command:  <br/>
<img src="https://i.imgur.com/rAHWZX8.png" height="80%" width="80%" alt="Details when users used su command"/>
<br />
<br />
Print details of users who used sudo command, including the command:  <br/>
<img src="https://i.imgur.com/OrFkx2C.png" height="80%" width="80%" alt="Print details of users who used sudo command, including the command"/>
<br />
<br />
Prints "ALERT!" if users failed to use the sudo command, including the command:  <br/>
<img src="https://i.imgur.com/04TaVCA.png" height="80%" width="80%" alt="Prints "ALERT!" if users failed to use the sudo command, including the command"/>
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
