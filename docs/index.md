---
title: Course Guide
layout: default
filename: index
--- 

A [GitHub Page](https://pages.github.com) to help the students navigate the Course material following the Class Workflow.

<h1>{{ page.title }}</h1>

<ul style="list-style: none;">
  {% for related in site.pages %}
    {% if related.url != page.url and related.dir == page.dir %}
      <li>
        <a href="{{ site.baseurl }}{{ related.url }}">{{ related.title }}</a>
      </li>
    {% endif %}
  {% endfor %}
</ul>

![Sir Hiss](https://raw.githubusercontent.com/tur-learning/CIS1051-python/gh-pages/lectures/notebooks/img/cis1051-cover.png)