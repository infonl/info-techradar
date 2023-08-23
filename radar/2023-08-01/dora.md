---
title: "DORA Metrics"
ring: adopt
quadrant: techniques
featured: true
---

The [DORA Metrics](https://cloud.google.com/blog/products/devops-sre/the-2019-accelerate-state-of-devops-elite-performance-productivity-and-scaling) (DevOps Research and Assessment) are a set of performance indicators that serve as an industry benchmark for evaluating the effectiveness of DevOps and software delivery performance.

They consist of four key metrics:
- **Deployment Frequency**: This metric measures how often a team deploys code to production. High-performing teams typically deploy more frequently, promoting smaller, manageable changes and quicker user feedback.
- **Lead Time for Changes**: This metric measures the time from when code is committed until it is deployed in production. A lower lead time indicates a more streamlined and efficient development and deployment process.
- **Change Failure Rate**: This measures the percentage of changes that fail in production. A lower change failure rate signifies higher code quality and reliable deployment practices.
- **Time to Restore Service**: This metric measures how quickly a team can recover from a failure in production. Quick restoration times demonstrate robust incident response processes.

Adopting the DORA metrics is advantageous for several reasons:
- **Benchmarking**: They provide an industry-standard measure of DevOps performance. 
- **Identifying Improvement Areas**: These metrics can help pinpoint where our practices need refinement.
- **Guiding Efficient Practices**: The metrics can steer us towards practices that increase productivity and efficiency.

Several tools can assist in tracking these metrics:

- [LinearB](https://linearb.io/) provides visibility into your development workflow, offering insights that help identify bottlenecks and improve efficiency. It can assist in measuring lead time and deployment frequency.
- [Apache DevLake](https://github.com/apache/incubator-dolphinscheduler) is an open-source tool aggregating data from various sources. It can centralize and streamline data collection, simplifying the calculation of DORA metrics.
- [Swarmia](https://swarmia.com/) offers analytics and insights into your software development processes. It provides detailed reports on various metrics, including the DORA metrics, helping identify trends and areas for improvement.

Creating a custom data lake can be beneficial for larger organizations with more complex requirements. A data lake allows for storing, integrating, and analyzing large amounts of raw data from various sources. This would offer us flexibility in calculating the DORA metrics and any other KPIs specific to our context, using tools of our choice for data extraction, storage, and analysis.

In conclusion, while the DORA metrics are a highly beneficial standard, we must remember to interpret them in the context of our teams, processes, and goals. They should serve as one component of a broader, holistic strategy for continuous improvement.
