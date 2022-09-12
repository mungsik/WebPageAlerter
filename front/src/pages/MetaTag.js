import { Helmet } from "react-helmet-async";

/**
 * 헤더 내용을 추가한다.
 * @param {string} props 웹 페이지 설명
 */

const MetaTag = (props) => {
  const baseURL = "http://localhost:3000";

  return (
    <Helmet>
      <title>{props.title}</title>

      <meta name="description" content={props.description} />
      <meta name="keywords" content={props.keywords} />
      <link rel="canonical" href={baseURL} />

      <meta property="og:type" content="website" />
      <meta property="og:title" content={props.title} />
      <meta property="og:site_name" content={props.title} />
      <meta property="og:description" content={props.description} />
      <meta property="og:image" content={props.imgsrc} />
      <meta property="og:url" content={props.url} />
    </Helmet>
  );
};

export default MetaTag;
