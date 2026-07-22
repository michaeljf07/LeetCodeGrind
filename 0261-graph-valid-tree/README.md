<h2><a href="[https://leetcode.com/problems/valid-anagram">261. Graph Valid Tree</a></h2><h3>Medium</h3><hr><p>Given <code>n</code> nodes labeled from <code>0</code> to <code>n - 1</code> and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.</p>

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<p>&nbsp;</p>
<p>You can assume that no duplicate edges will appear in edges. Since all edges are undirected, <code>[0, 1]</code> is the same as <code>[1, 0]</code> and thus will not appear together in edges.</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 <= n <= 100</code></li>
	<li><code>0 <= edges.length <= n * (n - 1) / 2</code></li>
</ul>
