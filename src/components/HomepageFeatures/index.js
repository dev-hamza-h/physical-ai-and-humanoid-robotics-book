import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Module 1: The Robotic Nervous System',
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        Learn the fundamentals of the Robot Operating System (ROS 2), the standard middleware for robotics.
      </>
    ),
  },
  {
    title: 'Module 2: The Digital Twin',
    Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        Dive into the world of simulation. You'll learn how to create a "digital twin" of your robot in realistic virtual environments.
      </>
    ),
  },
  {
    title: 'Module 3: The AI-Robot Brain',
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        Explore the AI techniques that give your robot intelligence, using NVIDIA's Isaac platform for perception and navigation.
      </>
    ),
  },
  {
    title: 'Module 4: Vision-Language-Action',
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        The capstone module. You'll build a complete voice-controlled robotics project, enabling you to command your robot using natural language.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--3')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
