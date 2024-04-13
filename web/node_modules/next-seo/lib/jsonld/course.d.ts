import React from 'react';
import type { Provider } from 'src/types';
import { JsonLdProps } from './jsonld';
export interface CourseJsonLdProps extends JsonLdProps {
    courseName: string;
    description: string;
    provider: Provider;
}
declare function CourseJsonLd({ type, keyOverride, courseName, provider, ...rest }: CourseJsonLdProps): React.JSX.Element;
export default CourseJsonLd;
